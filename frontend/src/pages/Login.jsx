import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { Container, TextField, Button, Typography, Box } from '@mui/material';
//import '../styles/Login.css';
import axios from 'axios'

function Login() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (event) => {
    event.preventDefault();
    try{
      const response = await axios.post('http://localhost:8000/api/login/', {username, password})
      console.log(response.data);
      localStorage.setItem("isAuthenticated", "true");
      navigate('/');
      
    }catch (error){
      setError("Invalid credentials")
    }
  };

  return (
    <Container maxWidth="sm" className="container">
      <Typography marginTop='30px' align='center'>Login</Typography>
      <Box component="form" onSubmit={handleSubmit} className="form">
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          id="username"
          label="Username"
          name="username"
          autoComplete="username"
          autoFocus
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />
        <TextField
          variant="outlined"
          margin="normal"
          required
          fullWidth
          name="password"
          label="Password"
          type="password"
          id="password"
          autoComplete="current-password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />
        {error && (
          <Typography className="error" variant="body2">
            {error}
          </Typography>
        )}
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          sx={{ mt: 3, mb: 2 }}
        >
          Login
        </Button>
      </Box>
    </Container>
  );
}

export default Login;
