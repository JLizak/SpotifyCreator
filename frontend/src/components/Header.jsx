import React, { useEffect, useState } from 'react';
import AppBar from '@mui/material/AppBar';
import Toolbar from '@mui/material/Toolbar';
import Button from '@mui/material/Button';
import { Link, useNavigate } from 'react-router-dom';
//import "../styles/Header.css"


function Header(){

    const [isAuthenticated, setIsAuthenticated] = useState(false);
    const navigate = useNavigate();

    useEffect(() => {
        const authStatus = localStorage.getItem('isAuthenticated');
        if (authStatus === 'true') {
          setIsAuthenticated(true);
        }
      });

      const handleLogout = () => {
        // Clear authentication state from local storage
        localStorage.removeItem('isAuthenticated');
        setIsAuthenticated(false);
        navigate('/');
      };

    return(
        <AppBar position="static" className="appBar">
            <Toolbar>
                <Button color="inherit" component={Link} to="/" >Home</Button>
                {isAuthenticated ? 
                (<Button color="inherit" onClick={handleLogout}> Logout </Button>) :
                (<Button color="inherit" component={Link} to="/login">Login </Button>)
                }
            </Toolbar>
        </AppBar>
    );
}

export default Header