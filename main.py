import happybase

# Connect to HBase via Thrift
connection = happybase.Connection('localhost', port=9090)
connection.open()
table = connection.table('practice:students')


for key, data in table.scan():
    print(key, data)

#Add a new row:
table.put(b'1003', {
    b'info:name': b'Charlie',
    b'info:age': b'22'
})

# READ DATA
row = table.row(b'1003')
print(row)


# UPDATE DATA (same as insert with existing key)
table.put(b'1003', {b'info:age': b'25'})  # Update age

# READ UPDATED DATA
row = table.row(b'1003')
print("Updated row:", row)

# DELETE DATA
#table.delete(b'1001')
#print("Row deleted.")


connection.close()
