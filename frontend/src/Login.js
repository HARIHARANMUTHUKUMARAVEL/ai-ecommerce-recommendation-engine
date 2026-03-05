import { useState } from "react";
import { loginUser } from "./api";

function Login({setUser,setPage}){

  const [username,setUsername] = useState("");
  const [password,setPassword] = useState("");

  const login = async () => {

    try{

      const res = await loginUser(username,password);

      alert(res.message);

      setUser(username);
      setPage("dashboard");

    }catch(err){

      alert("Invalid credentials");

    }

  };

  return(

    <div className="app-container">

      <h2>Login</h2>

      <input
      placeholder="Username"
      onChange={(e)=>setUsername(e.target.value)}
      />

      <input
      type="password"
      placeholder="Password"
      onChange={(e)=>setPassword(e.target.value)}
      />

      <button onClick={login}>Login</button>

      <p>
        Don't have account?
        <button onClick={()=>setPage("register")}>
        Register
        </button>
      </p>

    </div>

  );

}

export default Login;