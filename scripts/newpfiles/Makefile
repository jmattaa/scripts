cc=gcc

cflags=-Iinclude
cflagsdev=-g -Wall -Wextra -fsanitize=address $(cflags)
cflagsrel=-O3 $(cflags)
 
lflags=$(shell pkg-config --libs ncurses)
lflags_dev=-g -fsanitize=address $(lflags)
lflags_rel=$(lflags)
 
srcs=$(shell find src -name *.c)
dev_objs=$(patsubst src/%.c, $(build)/dev/%.o, $(srcs))
rel_objs=$(patsubst src/%.c, $(build)/rel/%.o, $(srcs))
 
build=build
dev_exec=__NEWP_PROJNAME__
rel_exec=$(build)/rel/__NEWP_PROJNAME__

dev: mkdirs $(dev_exec)
 
$(dev_exec): $(dev_objs)
    $(cc) $(lflags_dev) -o $@ $^
 
$(build)/dev/%.o: src/%.c
    $(cc) $(cflagsdev) -c -o $@ $<
 
rel: mkdirs $(rel_exec)
 
$(rel_exec): $(rel_objs)
    $(cc) $(lflags_rel) -o $@ $^
 
$(build)/rel/%.o: src/%.c
    $(cc) $(cflagsrel) -c -o $@ $<

clean:
    rm -rf $(build)
 
mkdirs:
    mkdir -p $(build)/dev
    mkdir -p $(build)/rel
