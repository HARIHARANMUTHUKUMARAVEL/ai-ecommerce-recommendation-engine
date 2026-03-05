import { useState } from "react";
import { registerUser } from "./api";

function Register({setPage}){

  const [username,setUsername] = useState("");
  const [password,setPassword] = useState("");

  const register = async () => {

    try{

      const res = await registerUser(username,password);

      alert(res.message);

      setPage("login");

    }catch(err){

      alert("Registration failed");

    }

  };

  return(

    <div className="app-container">

      <h2>Register</h2>

      <input
      placeholder="Username"
      onChange={(e)=>setUsername(e.target.value)}
      />

      <input
      type="password"
      placeholder="Password"
      onChange={(e)=>setPassword(e.target.value)}
      />

      <button onClick={register}>Register</button>

      <p>
        Already have account?
        <button onClick={()=>setPage("login")}>
        Login
        </button>
      </p>

    </div>

  );

}

export default Register;