char buff[64] = {"###111111111111111111111111111111111111111111111111111111111112X"};
// when reading this in python, the first index of buff array will not be sent
// why this is, I dont know, but it works
// should also have a special "buffer end" char so when we know what we should read and not

void setup() {

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print(buff); //64 bit
  
}
