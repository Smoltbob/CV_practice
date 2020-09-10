CC = clang++
CFLAGS = -g -Wall -Werror
LFLAGS = 
TARGET = main

all: $(TARGET)


$(TARGET): $(TARGET).cpp
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).cpp $(LFLAGS)

.PHONY: clean
clean :
	rm *.o $(TARGET)
