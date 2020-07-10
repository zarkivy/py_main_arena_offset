import os


def get_main_arena_offset( libc : str ) -> int :
    
    if not os.path.exists( libc ): 
        print("cannot open '" + libc + "' (No such file or directory)")
        return 0

    file_libc = get_output("file " + libc)
    if( file_libc.find("64-bit") == -1 ):
        return get_32_bit_main_arena_offset( libc )
    else:
        return get_64_bit_main_arena_offset( libc )



def get_32_bit_main_arena_offset( libc : str ) -> int :
    
    malloc_hook_str = get_output("objdump -j .data -d " + libc + "|grep __malloc_hook |cut -d' ' -f 1")
    malloc_hook = int(malloc_hook_str, 16)
    return malloc_hook + 0x18



def get_64_bit_main_arena_offset( libc : str ) -> int :
    
    malloc_hook_str = get_output("objdump -j .data -d " + libc + "|grep __malloc_hook |cut -d' ' -f 1")
    realloc_hook_str = get_output("objdump -j .data -d " + libc + "|grep __realloc_hook |cut -d' ' -f 1")
    malloc_hook = int(malloc_hook_str, 16)
    realloc_hook = int(realloc_hook_str, 16)
    return 3*malloc_hook - 2*realloc_hook



def get_output( command : str ) -> str :

    p = os.popen( command )
    s = p.read()
    p.close()
    return s



if __name__ == "__main__" :

    print(hex(get_main_arena_offset("./libc.so")))
