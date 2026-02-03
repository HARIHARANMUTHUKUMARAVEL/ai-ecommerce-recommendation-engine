import axios from "axios";

const API_URL = "http://localhost:5000/recommend";

export const getRecommendations = async (productId) => {
  const response = await axios.post(API_URL, {
    product_id: productId,
  });
  return response.data.recommended_products;
};
