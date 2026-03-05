import axios from "axios";

const API = "http://localhost:5000";

export const loginUser = async (username,password) => {

  const res = await axios.post(API+"/login",{
    username,
    password
  });

  return res.data;
};

export const registerUser = async (username,password) => {

  const res = await axios.post(API+"/register",{
    username,
    password
  });

  return res.data;
};

export const getRecommendations = async (productId) => {

  const res = await axios.post(API+"/recommend",{
    product_id: productId
  });

  return res.data.recommended_products;
};