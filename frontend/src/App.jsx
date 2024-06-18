import React from 'react';
import { Route, createBrowserRouter, createRoutesFromElements, RouterProvider} from 'react-router-dom';
import Home from './pages/Home';
import Login from './pages/Login';
import MainLayout from './layouts/MainLayout'

const router = createBrowserRouter(
  createRoutesFromElements(
  <Route path = '/' element={<MainLayout />}>
    <Route index element={<Home />} />
    <Route path='/login' element={<Login />} />
  </Route>
  ) 
);

function App() {
  return <RouterProvider router={router}/>;
}

export default App;
