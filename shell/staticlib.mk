CC ?= gcc
CFLAGS := -Wall -Werror -Wextra -pedantic
COBJFLAGS := $(CFLAGS) -c
ARFLAGS = rsv

INC_PATH := $(or $(headers), ../../include)
TARGET := $(or $(out_file), $(addsuffix .a, $(notdir $(shell pwd))))
SRCS := $(wildcard *.c)
OBJS := $(addsuffix .o, $(basename $(SRCS)))

default: $(TARGET) clean

$(TARGET): $(OBJS)
	ar $(ARFLAGS) $(TARGET) $(OBJS)

%.o: %.c
	$(CC) $(COBJFLAGS) -I$(INC_PATH) -o $@ $<

.PHONY: clean
clean:
	@rm -f $(OBJS)
