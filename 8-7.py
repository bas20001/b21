def make_album(singer,album_name,album_amount = ''):
	describe_album = {'musician':singer,'album':album_name}
	if album_amount :
		describe_album['album_amount'] = album_amount
	else :
		describe_album = {'musician':singer,'album':album_name}
	return describe_album
while True:
	print("make your own album on it")
	print("If you want to quit please input q")
	o_singer = raw_input('Input your singer name: \n')
	if o_singer == 'q':
		break
	o_album_name = raw_input('Input your album name: \n')
	if o_album_name == 'q':
		break
	o_album_amount = raw_input('Input your album_amount: \n')
	if o_album_amount == 'q':
		break

	album = make_album(o_singer,o_album_name,o_album_amount)
	print(album)
