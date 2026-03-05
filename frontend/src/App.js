import { useState } from "react";
import Login from "./Login";
import Register from "./Register";
import Dashboard from "./Dashboard";

function App(){

  const [page,setPage] = useState("login");
  const [user,setUser] = useState(null);

  if(page === "login")
    return <Login setUser={setUser} setPage={setPage}/>

  if(page === "register")
    return <Register setPage={setPage}/>

  return <Dashboard user={user}/>

}

export default App;