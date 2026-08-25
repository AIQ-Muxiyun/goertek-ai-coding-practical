#!/bin/sh
# 出题方新增的调试脚本（非上游文件）：回显请求方法 / Content-Length / body / query，便于联调。
# 注意：必须严格按 CONTENT_LENGTH 读取 body（读够即停），不能读至 EOF——
# 父进程在读完 CGI 全部输出后才会关闭 stdin 管道写端，读至 EOF 会互相等待造成死锁。
echo "Content-Type: text/plain"
echo ""
echo "method=$REQUEST_METHOD"
echo "content_length=${CONTENT_LENGTH:-0}"
if [ "$REQUEST_METHOD" = "POST" ]; then
    body=$(head -c "${CONTENT_LENGTH:-0}")
    echo "body=$body"
fi
echo "query=$QUERY_STRING"
