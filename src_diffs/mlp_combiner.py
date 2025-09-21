class BLIPCir(nn.Module):
    def __init__(
        #...
          hidden_dim=128,  ##### Hidden dimension for MLP #####
          combination_method = "MLP", ##### Method used to combine f(q,t), q and t in ["NA", "avg", "MLP"]#####
         ):
    #...
           
    ##### MLP to compute weights #####
    self.combination_method = combination_method
    if combination_method == "MLP":
        self.weight_predictor = nn.Sequential(
            nn.Linear(embed_dim * 3, hidden_dim),
            nn.ReLU(),
            nn.Linear(hidden_dim, 3),  # Output 3 weights
        )
    #...

    ###### Encode the ref image #######
    ref_img_feat = self.vision_proj(ref_img_embs[:, 0, :])  # [CLS] token
    ref_img_feat = F.normalize(ref_img_feat, dim=-1)
    #...

    ###### Encode the ref caption #######
    text_embs = self.text_encoder(
    input_ids=text.input_ids,
    attention_mask=text.attention_mask,
    return_dict=True,
    )
    text_feat = text_embs.last_hidden_state[:, 0, :]  # [CLS] token
    text_feat = F.normalize(self.text_proj(text_feat), dim=-1)
    #...


    ###### Combine embeddings: f(q, t), image embedding, and text embedding #######

    if self.combination_method == "NA":
        combined_feat = query_si_feat

    elif self.combination_method == "avg":
        # Combine features by averageing
        combined_feat = (query_si_feat + ref_img_feat + text_feat) / 3.0
        combined_feat = F.normalize(combined_feat, dim=-1)

    elif self.combination_method == "MLP":
        # Combine features with dynamic weights
        combined_input = torch.cat(
            [query_si_feat, ref_img_feat, text_feat], dim=-1
        )  # Concatenate embeddings
        weights = self.weight_predictor(combined_input)  # Predict weights
        weights = F.softmax(weights, dim=-1)  # Normalize weights

        combined_feat = (
            weights[:, 0:1] * query_si_feat
            + weights[:, 1:2] * ref_img_feat
            + weights[:, 2:3] * text_feat
        )
        combined_feat = F.normalize(combined_feat, dim=-1)
    #...
        
