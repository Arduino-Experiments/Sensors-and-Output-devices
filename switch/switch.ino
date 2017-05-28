auto LED=13;
auto SW=11;

void setup() {
    // put your setup code here, to run once:
    pinMode(LED,OUTPUT);
    pinMode(SW,HIGH);
}

void loop() {
    // put your main code here, to run repeatedly:
    auto val=digitalRead(SW);
    if(val){
        digitalWrite(LED,HIGH);
    }else{
        digitalWrite(LED,LOW);
    }
}
