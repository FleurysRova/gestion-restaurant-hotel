import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [users, setUsers] = useState([]);

  useEffect(() => {
    axios.get("http://backend:8000/")
      .then(res => setUsers(res.data))
      .catch(err => console.error(err));
  }, []);

  return (
    <div style={{ padding: "1rem" }}>
      <h1>Liste des utilisateurs</h1>
      {users.length === 0 && <p>Aucun utilisateur trouvé.</p>}
      <ul>
        {users.map(user => (
          <li key={user.user_id}>
            {user.user_name} {user.user_firstname} - {user.user_email}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
