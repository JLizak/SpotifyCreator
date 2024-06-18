import { createTheme } from '@mui/material/styles';
import { green, purple } from '@mui/material/colors';

const theme = createTheme({
    palette: {
      primary: {
        light: '#fafafa',
        main: '#1b5e20',
        dark: '#212121',
        contrastText: '#fafafa',
      },
      secondary: {
        light: '#ff7961',
        main: '#f44336',
        dark: '#ba000d',
        contrastText: '#000',
      },
    },
  });
  
  

export default theme;