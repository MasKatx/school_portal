const path = require("path");
const webpack = require("webpack");

module.exports = {
    entry: "./src/index.js",
    output: {
        // debundle main file -> npm run build
        path: path.resolve(__dirname, "./static/frontend"),
        filename: "[name].js",
    },
    module: {
        rules: [
            {
                //拡張子が.jsを検知したらbabelでES5に変換する
                test: /\.(js)$/,
                exclude: /node_modules/,
                use: {
                    loader: "babel-loader",
                    options: {
                        presets: ['@babel/preset-env', '@babel/preset-react']
                    }
                },
            },
            {
                //拡張子が.cssを検知したら
                test: /\.css$/,
                use: ["style-loader", "css-loader"]
            },
            {
                //拡張子がpng,jpg,gif,svgを検知したら
                test: /\.(png|jpg|gif|svg)/,
                use: [
                    {
                        loader: 'file-loader',
                        options: {
                            //[name]は画像名、[ext]は拡張子
                            name: 'images/[name].[ext]'
                        }
                    }
                ]
            }
        ],
    },
    optimization: {
        minimize: true,
    },
    plugins: [
        new webpack.DefinePlugin({
            // "process.env": {
            //     // This has effect on the react lib size
            //     NODE_ENV: JSON.stringify("production"),
            // },
            'process.env.NODE_ENV': JSON.stringify('development'),
        }),
    ],
    stats: {
        errorDetails: true,
        children: true
    },

};