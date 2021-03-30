// const vueConfig = {
//     css: {
//       loaderOptions: {
//         sass: {
//           data: `
//             @import "@/assets/style/fonts.scss";
//           `,
//         },
//       },
//     },
//   };




module.exports = {
    devServer: {
        proxy: {
            '/auth': {
                "target": "http://backend:80"
              }
        }
    }
}
