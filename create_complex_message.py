import complex_message_pb2

sub = complex_message_pb2.SubMessage
main = complex_message_pb2.MainMessage

main_message = main(
        main_id='Main1',
        sub_messages=[sub(id=1, content='Sub message 1'), 
                      sub(id=2, content='Sub message 2')]
    )
def create_complex_message():
    # Create MainMessage object containing the SubMessage objects
    main_message = main(
        main_id='Main1',
        sub_messages=[sub(id=1, content='Sub message 1'), 
                      sub(id=2, content='Sub message 2')]
    )
    return main_message

# Create a complex message and print it
print(main_message)
