const http = require('http')
const url = require('url')
const util = require('util')
const koa = require('koa')
const fs = require('fs')

let app = new koa();
app.listen(3000); //可自行修改监听端口
let exec = require('child_process').exec

//use()方法将中间件加入应用中
app.use(async function (ctx, next) {
    let url = ctx.url;
    let request = ctx.request;
    let req_query = request.query;
    let rText = req_query.content;
    let tMode = req_query.mode;
    if (url !== "/favicon.ico") {
        if (ctx.method === 'GET') {
            console.log("接收到GET请求！");
            result = await kksTrans(rText, tMode)
            let output = result.data
            console.log("GET请求处理成功！翻译返回结果为：" + result.data)
            ctx.body = {
                url,
                rText,
                output
            }
        } else if (ctx.method === 'POST') {
            console.log("接受到POST请求！")
            ctx.response.status = 200
            let postData = await paresPostData(ctx)
            ctx.body = postData
        }
    }
}
);
function kksTrans(rText, tMode) {
    let result = {};
    return new Promise(function (resolve, reject) {
        fs.writeFileSync("data.txt",rText)
        exec('python xnkakasi.py -'+tMode, function (err, output) {
            if (err) {
                console.log('出现错误：', err)
                result.data = err;
                resolve(result);
            } else {
                result.data = output;
                console.log("kks翻译结果为：",output)
                resolve(result);
            }
        })
    })
}
function paresPostData(ctx) {
    return new Promise((resolve, reject) => {
        let post_data = ''
        ctx.req.addListener('data', (postDataChunk) => {
            post_data += postDataChunk
        })
        ctx.req.addListener('end', async () => {
            // console.log('接受post数据完毕---->', post_data)
            result = await kksTrans(post_data, "ToRoma")
            console.log("POST请求处理成功！翻译返回结果为：" + result.data)
            output = result.data
            resolve(output)
        })
    })
}
//发生错误时触发
app.on('error', function (err) {
    console.log(err);
});
