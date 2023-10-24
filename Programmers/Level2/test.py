const int led[3] = {9, 10, 11};
const int bt = 2;

void setup() {
    for(int i=0;i<=2;i++) {
        pinMode(led[i], OUTPUT);
    }
    pinMode(bt, INPUT);
}

void loop() {
    int btsTate = digitalRead(bt);
    
    if(btState == HIGH) {
        for(int i=0;i<=2;i++) {
            analogWrite(led[i], HIGH);
            delay(10);
        }
    }
    else{
        for(int i=0;i<=2;i++) {
            analogWrite(led[i], LOW);
            delay(10);
        }
    }
}