// 在函数/方法/类级别上添加注释

void setup() {
  // 在此处放置设置代码，只运行一次:
  Serial.begin(9600);  // 初始化串行通信，并设置波特率为9600
  Serial.println("Hello World!\n");  // 发送字符串"Hello World!\n"到串行端口
}

void loop() {
  // 在此处放置主要代码，重复运行:
  if (Serial.available()){  // 如果串行端口可用
    int inByte = Serial.read();  // 从串行端口读取一个字节并存储在inByte中
    Serial.print("Read: ");  // 发送字符串"Read: "到串行端口
    Serial.print(inByte);  // 发送inByte的值到串行端口
    Serial.print(" Ox");  // 发送字符串" Ox"到串行端口
    Serial.println(inByte, HEX);  // 以十六进制形式发送inByte的值到串行端口并换行
  }
}