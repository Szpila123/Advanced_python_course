import text_compression

file_name = 'lorem_ipsum.txt'
compress_file = 'lorem_ipsum_compressed.txt'
if __name__ == '__main__':
    # Test run
    compress = text_compression.compress('suuuuper')
    decompress = text_compression.decompress(compress)
    
    if decompress != 'suuuuper':
        exit(1)

    # Load file content
    with open(file_name, 'r') as file:
        content = ' '.join(file.readlines())
    
    # Compress and save
    compress = text_compression.compress(content)
    text_compression.save(compress_file, compress)

    # Load and decompress
    compress = text_compression.load(compress_file)
    decompress = text_compression.decompress(compress)

    # Print after decompression (use 'diff -w' to compare with original file)
    print(decompress)


