import re

class Osu:

    @staticmethod
    def is_map_request(message: str):
        '''Checks if the message is a map request'''
        url_pattern = r'(https?:\/\/)?(osu|old).ppy.sh\/(p|b|beatmap|beatmaps|beatmapsets|s)\/(beatmap\?b=)?([\d]+#(osu|taiko|mania)\/[\d]+|[\d]+)(\&m=[\d])?'
        return True if re.findall(url_pattern, message) else False 
    
    @staticmethod
    def find_osu_url(message: str):
        '''Returns the osu url'''
        url_pattern = r'(https?:\/\/)?(osu|old).ppy.sh\/(p|b|beatmap|beatmaps|beatmapsets|s)\/(beatmap\?b=)?([\d]+#(osu|taiko|mania)\/[\d]+|[\d]+)(\&m=[\d])?'
        for str in message.split():
            if re.findall(url_pattern, str):
                return str
