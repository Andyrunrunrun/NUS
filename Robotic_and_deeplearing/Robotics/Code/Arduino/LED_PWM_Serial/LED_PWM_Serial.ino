// 定义引脚13为LED
#define LED 13

// 声明变量interval为整型，并标记为volatile
volatile int interval = 1;

void setup() {
  // 在此放置设置代码，仅运行一次
  // 设置引脚13为输出模式
  pinMode(LED, OUTPUT);

  // 初始化串行通信，波特率为9600
  Serial.begin(9600);
}

void loop() {
  int input = 0;
  
  // 在此放置主要代码，重复运行
  // 如果串行端口可用
  if (Serial.available()){
    // 读取串行数据到input
    input = Serial.read();
    // 如果input为'1'
    if (input == '1'){
      // interval增加5，限制在1到41之间
      interval = constrain(interval+5, 1, 41);
    } else {
      // interval减少5，限制在1到41之间
      interval = constrain(interval-5, 1, 41);
    }
  }
  
  // 将LED引脚输出高电平
  digitalWrite(LED, HIGH);
  // 延迟1毫秒
  delay(1);
  // 将LED引脚输出低电平
  digitalWrite(LED, LOW);
  // 延迟interval毫秒
  delay(interval);
}