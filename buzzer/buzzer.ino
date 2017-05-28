auto buzzerPort = 11;

void setup() {
    pinMode(buzzerPort,OUTPUT);
}

void loop() {
    while(true){
        /**
        第一个循环为1毫秒高电平1毫秒低电平.也就是2毫秒为一个周期,频率为500hz
        */
        for(auto i = 0;i<80;i++){
            digitalWrite(buzzerPort, HIGH);
            delay(1);
            digitalWrite(buzzerPort, LOW);
            delay(1);
        }
        /**
        第二个循环为2毫秒高电平2毫秒低电平.也就是4毫秒为一个周期,频率为250hz
        */
        for(auto i = 0;i<100;i++){
            digitalWrite(buzzerPort,HIGH);
            delay(2);
            digitalWrite(buzzerPort, LOW);
            delay(2);
        }
    }
}
