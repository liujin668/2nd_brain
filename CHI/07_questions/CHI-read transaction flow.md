![[Pasted image 20261013183226.png]]
为什么在3中readreceipt是可选的，在4中是必须的？
关键在于：HN 收到 RN 的 `CompAck` 时，能不能据此确认 SN 已经接受了下游读请求。第 3 种能，第 4 种未必。

在4中为什么compack可以在未收到datasepresp的情况下发送？data还没收到，而hn认为完成了，可能把后一笔的write发给sn，造成数据更新了再回给rn？
虽然rn回了compack，让hn有了进行同地址操作的权力，但是因为rn拿到了数，所以任何改动都需要发snp给rn，而不是直接修改sn里的数，所以rn在收到snp的时候回卡住，前一笔数一定要收到才能被snp掉，这样就使得整体顺序一定不会乱