locations = ['Tokyo', 'Paris', 'Italy', 'Prague', 'Edinburgh']

# urutan asli
print(locations)

# sorted() alfabet (list asli tidak berubah)
print(sorted(locations))

# bukti list masih urutan asli
print(locations)

# sorted() alfabet terbalik (list asli tidak berubah)
print(sorted(locations, reverse=True))

# bukti list masih urutan asli
print(locations)

# reverse() membalik urutan list secara permanen
locations.reverse()
print(locations)

# reverse() lagi, kembali ke urutan asli
locations.reverse()
print(locations)

# sort() mengurutkan list secara permanen (alfabet)
locations.sort()
print(locations)

# sort() mengurutkan list secara permanen (alfabet terbalik)
locations.sort(reverse=True)
print(locations)