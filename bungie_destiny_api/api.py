""" BungieAPI module """

import urllib2
import json
import ConfigParser
import os

# API_KEY = <secret API key>

# put a BungieNet API-KEY into a ini style file called 'bungie_api.cfg'
# in the cwd of the calling script

config_file = (os.path.join(os.getcwd(),'bungie_api.cfg'))
config = ConfigParser.ConfigParser()
config.read(config_file)
API_KEY = config.get('api', 'API-KEY')

# get_account https://www.bungie.net/platform/destiny/help/
# DEPRECATED use get_account_summary

def get_account(destiny_membership_id=None, membership_type=None
                , definitions=None):
    """get_account()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id
           + "/Summary/" + optional_arg +")")

    acct = call_bungie_api('/' + membership_type + '/Account/'
                           + destiny_membership_id + '/' + optional_arg)

    return acct



# get_account_summary https://www.bungie.net/platform/destiny/help/

def get_account_summary(destiny_membership_id=None, membership_type=None
                        , definitions=None):
    """get_account_summary()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Summary/" + optional_arg +")")

    acct_summary = call_bungie_api('/' + membership_type + '/Account/'
                                   + destiny_membership_id + '/Summary/'
                                   + optional_arg)

    return acct_summary

# get_activity_history_stats https://www.bungie.net/platform/destiny/help/

def get_activity_history_stats(destiny_membership_id=None
                               , membership_type=None, character_id=None
                               , definitions=None, page=None
                               , mode=None, count=None):
    """get_activity_history_stats()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    if mode is None:
        optional_arg = optional_arg + '&mode=None'
    else:
        optional_arg = optional_arg + '&mode=' + mode

    print ("DEBUG: call_bungie_api(/Stats/ActivityHistory/" + membership_type
           + "/" + destiny_membership_id + "/" + character_id + "/"
           + optional_arg +")")

    activity_history_stats = call_bungie_api('/Stats/ActivityHistory/'
                                             + membership_type + '/'
                                             + destiny_membership_id + '/'
                                             + character_id +'/'
                                             + optional_arg)

    return activity_history_stats

# get_account_advisors https://www.bungie.net/platform/destiny/help/

def get_account_advisors(destiny_membership_id=None, membership_type=None
                         , definitions=None):
    """get_account_advisors()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Advisors/" + optional_arg +")")

    acct_advisors = call_bungie_api('/' + membership_type + '/Account/'
                                    + destiny_membership_id + '/Advisors/'
                                    + optional_arg)

    return acct_advisors

# get_account_advisors_v2 https://www.bungie.net/platform/destiny/help/

def get_account_advisors_v2(destiny_membership_id=None, membership_type=None
                            , character_id=None, definitions=None):
    """get_account_adviors()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/" + character_id
           + "/Advisors/V2/" + optional_arg +")")

    acct_advisors_v2 = call_bungie_api('/' + membership_type + '/Account/'
                                       + destiny_membership_id + '/Character/'
                                       + character_id + '/Advisors/V2/'
                                       + optional_arg)

    return acct_advisors_v2

# get_account_items https://www.bungie.net/platform/destiny/help/

def get_account_items(destiny_membership_id=None, membership_type=None
                      , definitions=None):
    """get_account_items()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Items/" + optional_arg +")")

    acct_items = call_bungie_api('/' + membership_type + '/Account/'
                                 + destiny_membership_id + '/items/'
                                 + optional_arg)

    return acct_items

# get_character_activities https://www.bungie.net/platform/destiny/help/

def get_character_activities(destiny_membership_id=None, membership_type=None
                            , character_id=None, definitions=None):
    """get_character_activities()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/"
           + character_id + "/Activities/" + optional_arg +")")

    char_activities = call_bungie_api('/' + membership_type + '/Account/'
                                      + destiny_membership_id + '/Character/'
                                      + character_id + '/Activities/'
                                      + optional_arg)

    return char_activities

# get_character_inventory https://www.bungie.net/platform/destiny/help/
# DEPREATED use get_character_inventorySummary instead!

def get_character_inventory(destiny_membership_id=None, membership_type=None
                            , character_id=None, definitions=None):
    """get_character_inventory()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/"
           + character_id + "/Inventory/" + optional_arg +")")

    char_inventory = call_bungie_api('/' + membership_type + '/Account/'
                                     + destiny_membership_id + '/Character/'
                                     + character_id + '/Inventory/'
                                     + optional_arg)

    return char_inventory

# get_character_inventory_summary https://www.bungie.net/platform/destiny/help/

def get_character_inventory_summary(destiny_membership_id=None
                                    , membership_type=None
                                    , character_id=None, definitions=None):
    """get_character_inventory_summary()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/"
           + character_id + "/Inventory/Summary/"
           + optional_arg +")")

    char_inventory_summary = call_bungie_api('/' + membership_type
                                             + '/Account/'
                                             + destiny_membership_id
                                             + '/Character/'
                                             + character_id
                                             + '/Inventory/Summary/'
                                             + optional_arg)

    return char_inventory_summary

# get_character_progression https://www.bungie.net/platform/destiny/help/

def get_character_progression(destiny_membership_id=None, membership_type=None
                              , character_id=None, definitions=None):
    """get_character_progression()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/"
           + character_id + "/Progression/"
           + optional_arg +")")

    char_progression = call_bungie_api('/' + membership_type + '/Account/'
                                       + destiny_membership_id + '/Character/'
                                       + character_id + '/Progression/'
                                       + optional_arg)

    return char_progression

# get_character_summary https://www.bungie.net/platform/destiny/help/

def get_character_summary(destiny_membership_id=None, membership_type=None
                          , character_id=None, definitions=None):
    """get_character_summary()"""


    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/" + membership_type + "/Account/"
           + destiny_membership_id + "/Character/"
           + character_id + "/" + optional_arg +")")

    char_summary = call_bungie_api('/' + membership_type + '/Account/'
                                   + destiny_membership_id + '/Character/'
                                   + character_id + '/' + optional_arg)

    return char_summary

# get_character_aggregate_stats at
# https://www.bungie.net/platform/destiny/help/

def get_character_aggregate_stats(destiny_membership_id=None
                                  , membership_type=None
                                  , character_id=None
                                  , definitions=None):
    """get_character_aggregate_stats()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/Stats/AggregateActivityStats/"
           + membership_type + "/" + destiny_membership_id + "/"
           + character_id + "/" + optional_arg +")")

    char_agg_activity_stats = call_bungie_api('/Stats/AggregateActivityStats/'
                                              + membership_type + '/'
                                              + destiny_membership_id + '/'
                                              + character_id + '/'
                                              + optional_arg)

    return char_agg_activity_stats

# get_character_stats https://www.bungie.net/platform/destiny/help/

def get_character_stats(destiny_membership_id=None, membership_type=None
                        , character_id=None, dayend=None, modes=None
                        , period_type=None, groups=None, monthstart=None
                        , monthend=None, daystart=None):
    """get_character_stats()"""

    if modes is None:
        optional_arg = '?modes=None'
    else:
        optional_arg = '?modes=' + modes

    print ("DEBUG: call_bungie_api(/Stats/" + membership_type + "/"
           + destiny_membership_id + "/" + character_id + "/"
           + optional_arg + ")")

    char_stats = call_bungie_api('/Stats/' + membership_type + '/'
                                 + destiny_membership_id + '/'
                                 + character_id + '/' + optional_arg)

    return char_stats

# get_account_stats https://www.bungie.net/platform/destiny/help/

def get_account_stats(destiny_membership_id=None, membership_type=None
                      , groups=None):
    """get_account_stats()"""

    if groups is None:
        optional_arg = ''
    else:
        optional_arg = '?groups=' + groups

    print ("DEBUG: call_bungie_api(/Stats/Account/" + membership_type + "/"
           + destiny_membership_id + "/" + optional_arg + ")")

    acct_stats = call_bungie_api('/Stats/Account/' + membership_type + '/'
                                 + destiny_membership_id + '/'
                                 + optional_arg)

    return acct_stats

# get_activity_stats https://www.bungie.net/platform/destiny/help/

def get_activity_stats(activity_id=None, definitions=None):
    """get_activity_stats()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/Stats/PostGameCarnageReport/"
           + activity_id + "/" + optional_arg + ")")

    activity_pgc_report_stats = call_bungie_api('/Stats/PostGameCarnageReport/'
                                                + activity_id + '/'
                                                + optional_arg)

    return activity_pgc_report_stats

# get_char_uniq_weapon_stats at
# https://www.bungie.net/platform/destiny/help/

def get_char_uniq_weapon_stats(membership_type=None
                               , destiny_membership_id=None
                               , character_id=None
                               , definitions=None):
    """get_char_uniq_weapon_stats()"""

    if definitions is None:
        optional_arg = ''
    else:
        optional_arg = '?definitions=true'

    print ("DEBUG: call_bungie_api(/Stats/UniqueWeapons/"
           + membership_type + "/" + destiny_membership_id + "/"
           + character_id + "/" + optional_arg + ")")

    char_uniq_weapon_stats = call_bungie_api('/Stats/UniqueWeapons/'
                                             + membership_type + '/'
                                             + destiny_membership_id + '/'
                                             + character_id + '/'
                                             + optional_arg)

    return char_uniq_weapon_stats

def call_bungie_api(method):
    """call_bungie_api()"""

    # takes a BungieNet API method as documented at
    # https://www.bungie.net/platform/destiny/help/

    api_base = 'https://www.bungie.net/Platform/Destiny'
    call_url = api_base + method

    request = urllib2.Request(call_url, headers={'X-API-Key':API_KEY})

    result = urllib2.urlopen(request).read().decode('utf-8')

    parsed_result = json.loads(result)

    return parsed_result

def get_characters(destiny_membership_id=None, membership_type=None):
    """get_characters()"""

    _summary = call_bungie_api('/' + membership_type + '/Account/'
                               + destiny_membership_id + '/Summary/')

    print _summary

    _character_1 = _summary['Response']['data']['characters'][0]\
            ['characterBase']['characterId']
    _character_2 = _summary['Response']['data']['characters'][1]\
            ['characterBase']['characterId']
    _character_3 = _summary['Response']['data']['characters'][2]\
            ['characterBase']['characterId']

    _character = [_character_1, _character_2, _character_3]

    return _character
