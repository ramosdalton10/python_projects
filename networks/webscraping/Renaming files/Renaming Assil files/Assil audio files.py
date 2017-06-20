import os

# print os.getcwd()
os.chdir('/root/Music/Audio/german2')
# # print os.getcwd()
# num_padded = []
# ##########THIS PART IS COMPLETED
# for mp3 in os.listdir('/root/Music/Audio/german4'):
#     sin_mp3 = mp3.split('.mp3')[0]
#     num = sin_mp3.split('-')[1]
#     if len (num) < 2:
#         zero_fill = num.zfill(2)
#         num_padded.append(num.zfill(2))
#         new_name = 'German4-'+zero_fill+'.mp3'
#         os.rename(mp3,new_name)
#
#     else:
#         num_padded.append(num)
#         new_name = 'German4-' + num + '.mp3'
#         os.rename(mp3, new_name)


#
#
# for mp3 in os.listdir('/root/Music/Audio/german4'):
#     sin_mp3 = mp3.split('.')[0]
#     # print sin_mp3
#     nums = sin_mp3.split('-')[1]
#     new_name = nums+'_German_4.mp3'
#     os.rename(mp3,new_name)
# ##################################   THIS ABOVE PART IS COMPLETED#
# # ######################################################
#
#
# dict_data = {}
# i = 1
# y = 27
# staerting_num = []
#
# for mp3 in os.listdir('/root/Music/Audio/german2'):
#
#     dict_data[str(i).zfill(2)] = str(y)
#     i += 1
#     y += 1
# for mp3 in os.listdir('/root/Music/Audio/german2'):
#     x = mp3.split('_')[0]
#     new_name = dict_data[x]+'_German_2.mp3'
#     os.rename(mp3,new_name)
#     print mp3
# print dict_data


