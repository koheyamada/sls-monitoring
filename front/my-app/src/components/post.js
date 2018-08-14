const axios = require('axios');

const data = { name : 'Yohei', slack : 'Munesada' };
axios.post('https://gxni4w9ak1.execute-api.ap-northeast-1.amazonaws.com/putItems/', data).then(response => {
    console.log('body:', response.data);  // Yohei Munesada
});
