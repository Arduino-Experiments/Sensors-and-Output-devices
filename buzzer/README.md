# 蜂鸣器实验

除了可以输入输出数字信号,arduino还可以输入输出模拟信号.

## 器材

1. 无源蜂鸣器

无源蜂鸣器的发声原理就是根据高低电频的频率来发出特定频率的声音.因此每个声音都是用循环产生的.


## 接法

直接将蜂鸣器的两个针角插在GND和11号口上

## 程序

本程序使用数字输入输出端口的11号口,程序如下:

```C++

auto buzzerPort = 11;

void setup() {
    pinMode(buzzerPort,OUTPUT);
}

void loop() {
    while(true){
        //第一个循环为1毫秒高电平1毫秒低电平.也就是2毫秒为一个周期,频率为500hz

        for(auto i = 0;i<80;i++){
            digitalWrite(buzzerPort, HIGH);
            delay(1);
            digitalWrite(buzzerPort, LOW);
            delay(1);
        }

        //第二个循环为2毫秒高电平2毫秒低电平.也就是4毫秒为一个周期,频率为250hz

        for(auto i = 0;i<100;i++){
            digitalWrite(buzzerPort,HIGH);
            delay(2);
            digitalWrite(buzzerPort, LOW);
            delay(2);
        }
    }
}
```
