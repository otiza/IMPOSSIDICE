def split_range_into_chunks(start_hex, end_hex, num_chunks):
    start = int(start_hex, 16)
    end = int(end_hex, 16)
    total_range = end - start + 1
    chunk_size = total_range // num_chunks
    chunks = []

    for chunk in range(num_chunks):
        chunk_start = start + chunk * chunk_size
        chunk_end = chunk_start + chunk_size - 1 if chunk < num_chunks - 1 else end
        chunks.append((chunk_start, chunk_end))

    return chunks

if __name__ == "__main__":
    start_hex = "0000000000000000000000000000000000000000000000000000000000000400"
    end_hex = "00000000000000000000000000000000000000000000000000000000000007ff"
    num_chunks = 5

    chunks = split_range_into_chunks(start_hex, end_hex, num_chunks)
    with open(f"chunk_sss.txt", "w") as f:
        for i, (chunk_start, chunk_end) in enumerate(chunks):
            f.write(f"{hex(chunk_start)},{hex(chunk_end)}\n")
            print(f"{hex(chunk_start)},{hex(chunk_end)}\n")