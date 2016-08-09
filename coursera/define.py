# -*- coding: utf-8 -*-

"""
This module defines the global constants.
"""

import os
import getpass
import tempfile

COURSERA_URL = 'https://www.coursera.org'
AUTH_URL = 'https://accounts.coursera.org/api/v1/login'
AUTH_URL_V3 = 'https://www.coursera.org/api/login/v3'
CLASS_URL = 'https://class.coursera.org/{class_name}'

# The following link is left just for illustative purposes:
# https://www.coursera.org/api/courses.v1?fields=display%2CpartnerIds%2CphotoUrl%2CstartDate%2Cpartners.v1(homeLink%2Cname)&includes=partnerIds&q=watchlist&start=0
# Reply is as follows:
# {
#     "elements": [
#         {
#             "courseType": "v1.session",
#             "name": "Computational Photography",
#             "id": "v1-87",
#             "slug": "compphoto"
#         }
#     ],
#     "paging": {
#         "next": "100",
#         "total": 154
#     },
#     "linked": {}
# }
OPENCOURSE_LIST_COURSES = 'https://www.coursera.org/api/courses.v1?q=watchlist&start={start}'

# The following link is left just for illustative purposes:
# https://www.coursera.org/api/memberships.v1?fields=courseId,enrolledTimestamp,grade,id,lastAccessedTimestamp,onDemandSessionMembershipIds,onDemandSessionMemberships,role,v1SessionId,vc,vcMembershipId,courses.v1(courseStatus,display,partnerIds,photoUrl,specializations,startDate,v1Details,v2Details),partners.v1(homeLink,name),v1Details.v1(sessionIds),v1Sessions.v1(active,certificatesReleased,dbEndDate,durationString,hasSigTrack,startDay,startMonth,startYear),v2Details.v1(onDemandSessions,plannedLaunchDate,sessionsEnabledAt),specializations.v1(logo,name,partnerIds,shortName)&includes=courseId,onDemandSessionMemberships,vcMembershipId,courses.v1(partnerIds,specializations,v1Details,v2Details),v1Details.v1(sessionIds),v2Details.v1(onDemandSessions),specializations.v1(partnerIds)&q=me&showHidden=true&filter=current,preEnrolled
# Sample reply:
# {
#     "elements": [
#         {
#             id: "4958~bVgqTevEEeWvGQrWsIkLlw",
#             userId: 4958,
#             courseId: "bVgqTevEEeWvGQrWsIkLlw",
#             role: "LEARNER"
#         },
#     ],
#     "paging": null,
#     "linked": {
#         "courses.v1": [
#             {
#                 "id": "0w0JAG9JEeSp0iIAC12Jpw",
#                 "slug": "computational-neurosciencecompneuro",
#                 "courseType": "v2.ondemand",
#                 "name": "Computational Neuroscience"
#             }
#         ]
#     }
# }
OPENCOURSE_MEMBERSHIPS = 'https://www.coursera.org/api/memberships.v1?includes=courseId,courses.v1&q=me&showHidden=true&filter=current,preEnrolled'
OPENCOURSE_CONTENT_URL = 'https://www.coursera.org/api/opencourse.v1/course/{class_name}?showLockedItems=true'
OPENCOURSE_VIDEO_URL = 'https://www.coursera.org/api/opencourse.v1/video/{video_id}'
OPENCOURSE_SUPPLEMENT_URL = 'https://www.coursera.org/api/onDemandSupplements.v1/'\
    '{course_id}~{element_id}?includes=asset&fields=openCourseAssets.v1%28typeName%29,openCourseAssets.v1%28definition%29'
OPENCOURSE_PROGRAMMING_ASSIGNMENTS_URL = \
    'https://www.coursera.org/api/onDemandProgrammingLearnerAssignments.v1/{course_id}~{element_id}?fields=submissionLearnerSchema'

# These are ids that are present in <asset> tag in assignment text:
#
# <asset id=\"yeJ7Q8VAEeWPRQ4YsSEORQ\"
#        name=\"statement-pca\"
#        extension=\"pdf\"
#        assetType=\"generic\"/>
#
# Sample response:
#
# {
#   "elements": [
#     {
#       "id": "yeJ7Q8VAEeWPRQ4YsSEORQ",
#       "url": "<some url>",
#       "expires": 1454371200000
#     }
#   ],
#   "paging": null,
#   "linked": null
# }
OPENCOURSE_ASSET_URL = \
    'https://www.coursera.org/api/assetUrls.v1?ids={ids}'

# These ids are provided in lecture json:
#
# {
#   "id": "6ydIh",
#   "name": "Введение в теорию игр",
#   "elements": [
#     {
#       "id": "ujNfj",
#       "name": "Что изучает теория игр?",
#       "content": {
#         "typeName": "lecture",
#         "definition": {
#           "duration": 536000,
#           "videoId": "pGNiQYo-EeWNvA632PIn3w",
#           "optional": false,
#           "assets": [
#             "giAxucdaEeWJTQ5WTi8YJQ@1"
#           ]
#         }
#       },
#       "slug": "chto-izuchaiet-tieoriia-ighr",
#       "timeCommitment": 536000
#     }
#   ],
#   "slug": "vviedieniie-v-tieoriiu-ighr",
#   "timeCommitment": 536000,
#   "optional": false
# }
#
# Sample response:
#
# {
#   "elements": [
#     {
#       "id": "giAxucdaEeWJTQ5WTi8YJQ",
#       "typeName": "asset",
#       "definition": {
#         "name": "",
#         "assetId": "Vq8hwsdaEeWGlA7xclFASw"
#       }
#     }
#   ],
#   "paging": null,
#   "linked": null
# }
OPENCOURSE_ASSETS_URL = \
    'https://www.coursera.org/api/openCourseAssets.v1/{id}'

# These asset ids are ids returned from OPENCOURSE_ASSETS_URL request:
# See example above.
#
# Sample response:
#
# {
#   "elements": [
#     {
#       "id": "Vq8hwsdaEeWGlA7xclFASw",
#       "name": "1_Strategic_Interactions.pdf",
#       "typeName": "generic",
#       "url": {
#         "url": "<some url>",
#         "expires": 1454371200000
#       }
#     }
#   ],
#   "paging": null,
#   "linked": null
# }
OPENCOURSE_API_ASSETS_V1_URL = \
    'https://www.coursera.org/api/assets.v1?ids={id}'

OPENCOURSE_ONDEMAND_COURSE_MATERIALS = \
    'https://www.coursera.org/api/onDemandCourseMaterials.v1/?'\
        'q=slug&slug={class_name}&includes=moduleIds%2ClessonIds%2CpassableItemGroups%2CpassableItemGroupChoices%2CpassableLessonElements%2CitemIds%2Ctracks'\
        '&fields=moduleIds%2ConDemandCourseMaterialModules.v1(name%2Cslug%2Cdescription%2CtimeCommitment%2ClessonIds%2Coptional)%2ConDemandCourseMaterialLessons.v1(name%2Cslug%2CtimeCommitment%2CelementIds%2Coptional%2CtrackId)%2ConDemandCourseMaterialPassableItemGroups.v1(requiredPassedCount%2CpassableItemGroupChoiceIds%2CtrackId)%2ConDemandCourseMaterialPassableItemGroupChoices.v1(name%2Cdescription%2CitemIds)%2ConDemandCourseMaterialPassableLessonElements.v1(gradingWeight)%2ConDemandCourseMaterialItems.v1(name%2Cslug%2CtimeCommitment%2Ccontent%2CisLocked%2ClockableByItem%2CitemLockedReasonCode%2CtrackId)%2ConDemandCourseMaterialTracks.v1(passablesCount)'\
        '&showLockedItems=true'

ABOUT_URL = ('https://api.coursera.org/api/catalog.v1/courses?'
             'fields=largeIcon,photo,previewLink,shortDescription,smallIcon,'
             'smallIconHover,universityLogo,universityLogoSt,video,videoId,'
             'aboutTheCourse,targetAudience,faq,courseSyllabus,courseFormat,'
             'suggestedReadings,instructor,estimatedClassWorkload,'
             'aboutTheInstructor,recommendedBackground,subtitleLanguagesCsv&'
             'q=search&query={class_name}')

AUTH_REDIRECT_URL = ('https://class.coursera.org/{class_name}'
                     '/auth/auth_redirector?type=login&subtype=normal')

#POST_OPENCOURSE_API_QUIZ_SESSION = 'https://www.coursera.org/api/opencourse.v1/user/4958/course/text-mining/item/7OQHc/quiz/session'
# Sample response:
#
# {
#   "contentResponseBody": {
#     "session": {
#       "id": "opencourse~bVgqTevEEeWvGQrWsIkLlw:4958:BiNDdOvPEeWAkwqbKEEh3w@13:1468773901987@1",
#       "open": true
#     }
#   },
#   "itemProgress": {
#     "contentVersionedId": "BiNDdOvPEeWAkwqbKEEh3w@13",
#     "timestamp": 1468774458435,
#     "progressState": "Started"
#   }
# }
POST_OPENCOURSE_API_QUIZ_SESSION = 'https://www.coursera.org/api/opencourse.v1/user/{user_id}/course/{class_name}/item/{quiz_id}/quiz/session'

#POST_OPENCOURSE_API_QUIZ_SESSION_GET_STATE = 'https://www.coursera.org/api/opencourse.v1/user/4958/course/text-mining/item/7OQHc/quiz/session/opencourse~bVgqTevEEeWvGQrWsIkLlw:4958:BiNDdOvPEeWAkwqbKEEh3w@13:1468773901987@1/action/getState?autoEnroll=false'
# Sample response:
#
# {
#   "contentResponseBody": {
#     "return": {
#       "questions": [
#         {
#           "id": "89424f6873744b5c0b92da2936327bb4",
#           "question": {
#             "type": "mcq"
#           },
#           "variant": {
#             "definition": {
#               "prompt": {
#                 "typeName": "cml",
#                 "definition": {
#                   "dtdId": "assess/1",
#                   "value": "<co-content><text hasMath=\"true\">You are given a unigram language model $$\\theta$$ distributed over a vocabulary set $$V$$ composed of <strong>only</strong> 4 words: “the”, “machine”, “learning”, and “data”. The distribution of $$\\theta$$ is given in the table below:</text><table rows=\"5\" columns=\"2\"><tr><th><text>$$w$$</text></th><th><text>$$P(w|\\theta)$$</text></th></tr><tr><td><text>machine</text></td><td><text>0.1</text></td></tr><tr><td><text>learning</text></td><td><text>0.2</text></td></tr><tr><td><text>data</text></td><td><text>0.3</text></td></tr><tr><td><text>the</text></td><td><text>0.4</text></td></tr></table><text hasMath=\"true\"> $$P(\\text{“machine learning”}|\\theta) = $$</text></co-content>"
#                 }
#               },
#               "options": [
#                 {
#                   "id": "717bd78dec2b817bed4b2d6096cbc9fc",
#                   "display": {
#                     "typeName": "cml",
#                     "definition": {
#                       "dtdId": "assess/1",
#                       "value": "<co-content><text>0.004</text></co-content>"
#                     }
#                   }
#                 },
#                 {
#                   "id": "a06c614cbb15b4e54212296b16fc4e62",
#                   "display": {
#                     "typeName": "cml",
#                     "definition": {
#                       "dtdId": "assess/1",
#                       "value": "<co-content><text>0.2</text></co-content>"
#                     }
#                   }
#                 },
#                 {
#                   "id": "029fe0fee932d6ad260f292dd05dc5c9",
#                   "display": {
#                     "typeName": "cml",
#                     "definition": {
#                       "dtdId": "assess/1",
#                       "value": "<co-content><text>0.3</text></co-content>"
#                     }
#                   }
#                 },
#                 {
#                   "id": "b6af6403d4ddde3b1e58599c12b6397a",
#                   "display": {
#                     "typeName": "cml",
#                     "definition": {
#                       "dtdId": "assess/1",
#                       "value": "<co-content><text>0.02</text></co-content>"
#                     }
#                   }
#                 }
#               ]
#             },
#             "detailLevel": "Full"
#           },
#           "weightedScoring": {
#             "maxScore": 1
#           },
#           "isSubmitAllowed": true
#         }
#       ],
#       "evaluation": null
#     }
#   },
#   "itemProgress": {
#     "contentVersionedId": "BiNDdOvPEeWAkwqbKEEh3w@13",
#     "timestamp": 1468774458894,
#     "progressState": "Started"
#   }
# }
#
POST_OPENCOURSE_API_QUIZ_SESSION_GET_STATE = 'https://www.coursera.org/api/opencourse.v1/user/{user_id}/course/{class_name}/item/{quiz_id}/quiz/session/{session_id}/action/getState?autoEnroll=false'

#POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS = 'https://www.coursera.org/api/onDemandExamSessions.v1/-N44X0IJEeWpogr5ZO8qxQ~YV0W4~10!~1467462079068/actions?includes=gradingAttempts'
# Sample response:
#
# {
#   "elements": [
#     {
#       "id": 0,
#       "result": {
#         "questions": [
#           {
#             "id": "8uUpMzm_EeaetxLgjw7H8Q@0",
#             "question": {
#               "type": "mcq"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nSuppose you’d like to perform nearest neighbor search from the following set of houses:</text><table rows=\"5\" columns=\"4\"><tr><td><text>\n\n\n\n\n\n</text></td><td><text>\n\n\nPrice (USD)</text></td><td><text>\n\n\nNumber of rooms</text></td><td><text>\n\n\nLot size (sq. ft.)</text></td></tr><tr><td><text>\n\n\nHouse 1</text></td><td><text>\n\n\n500000</text></td><td><text>\n\n\n3</text></td><td><text>\n\n\n1840</text></td></tr><tr><td><text>\n\n\nHouse 2</text></td><td><text>\n\n\n350000</text></td><td><text>\n\n\n2</text></td><td><text>\n\n\n1600</text></td></tr><tr><td><text>House 3</text></td><td><text>\n\n600000</text></td><td><text>\n\n4</text></td><td><text>\n\n2000</text></td></tr><tr><td><text>House 4</text></td><td><text>\n400000</text></td><td><text>\n2</text></td><td><text>\n1900</text></td></tr></table><text>\n\nSince the features come in wildly different scales, you decide to use scaled Euclidean distances. Choose the set of weights a_i (as presented in the video lecture) that properly incorporates the relative amount of variation of the feature.</text><text>Note: </text><code language=\"plain_text\">a_price = weight assigned to price (USD)\na_room  = weight assigned to number of rooms\na_lot   = weight assigned to lot size (sq.ft.)</code></co-content>"
#                   }
#                 },
#                 "options": [
#                   {
#                     "id": "0.9109180361318947",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1, a_room = 1, a_lot = 1</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.11974743029080992",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1, a_room = 1, a_lot = 1e-6</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.8214165539451299",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e-10, a_room = 1, a_lot = 1e-6</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.6784789645868041",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e-5, a_room = 1, a_lot = 1e-3</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.9664001374497642",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e5, a_room = 1, a_lot = 1e3</text></co-content>"
#                       }
#                     }
#                   }
#                 ]
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "jeVDBjnNEeaetxLgjw7H8Q@0",
#             "question": {
#               "type": "singleNumeric"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nConsider the following two sentences.\n</text><list bulletType=\"bullets\"><li><text>Sentence 1: The quick brown fox jumps over the lazy dog.\n</text></li><li><text>Sentence 2: A quick brown dog outpaces a quick fox.\n</text></li></list><text>\n\nCompute the Euclidean distance using word counts. Round your answer to 3 decimal places.</text><text>Note. To compute word counts, turn all words into lower case and strip all punctuation, so that \"The\" and \"the\" are counted as the same token.</text></co-content>"
#                   }
#                 }
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "-tI-EjnNEeaPCw5NUSdt1w@0",
#             "question": {
#               "type": "singleNumeric"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>Refer back to the two sentences given in Question 2 to answer the following:</text><text>Recall that we can use cosine similarity to define a distance.  We call that distance cosine distance. </text><text>Compute the <strong>cosine distance</strong> using word counts. Round your answer to 3 decimal places.\n</text><text>Note: To compute word counts, turn all words into lower case and strip all punctuation, so that \"The\" and \"the\" are counted as the same token.</text><text>Hint. Recall that we can use cosine similarity to define a distance.  We call that distance cosine distance.</text></co-content>"
#                   }
#                 }
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           }
#         ],
#         "evaluation": null
#       }
#     }
#   ],
#   "paging": null,
#   "linked": {
#     "gradingAttempts.v1": []
#   }
# }
#
# Request payload:
# {"courseId":"-N44X0IJEeWpogr5ZO8qxQ","itemId":"YV0W4"}
#
#POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS = 'https://www.coursera.org/api/onDemandExamSessions.v1/-N44X0IJEeWpogr5ZO8qxQ~YV0W4~10!~1467462079068/actions?includes=gradingAttempts'

# Response for this request is empty. Result (session_id) should be taken
# either from Location header or from X-Coursera-Id header.
#
# Request payload:
# {"courseId":"-N44X0IJEeWpogr5ZO8qxQ","itemId":"YV0W4"}
POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS = 'https://www.coursera.org/api/onDemandExamSessions.v1'

# Sample response:
# {
#   "elements": [
#     {
#       "id": 0,
#       "result": {
#         "questions": [
#           {
#             "id": "8uUpMzm_EeaetxLgjw7H8Q@0",
#             "question": {
#               "type": "mcq"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nSuppose you’d like to perform nearest neighbor search from the following set of houses:</text><table rows=\"5\" columns=\"4\"><tr><td><text>\n\n\n\n\n\n</text></td><td><text>\n\n\nPrice (USD)</text></td><td><text>\n\n\nNumber of rooms</text></td><td><text>\n\n\nLot size (sq. ft.)</text></td></tr><tr><td><text>\n\n\nHouse 1</text></td><td><text>\n\n\n500000</text></td><td><text>\n\n\n3</text></td><td><text>\n\n\n1840</text></td></tr><tr><td><text>\n\n\nHouse 2</text></td><td><text>\n\n\n350000</text></td><td><text>\n\n\n2</text></td><td><text>\n\n\n1600</text></td></tr><tr><td><text>House 3</text></td><td><text>\n\n600000</text></td><td><text>\n\n4</text></td><td><text>\n\n2000</text></td></tr><tr><td><text>House 4</text></td><td><text>\n400000</text></td><td><text>\n2</text></td><td><text>\n1900</text></td></tr></table><text>\n\nSince the features come in wildly different scales, you decide to use scaled Euclidean distances. Choose the set of weights a_i (as presented in the video lecture) that properly incorporates the relative amount of variation of the feature.</text><text>Note: </text><code language=\"plain_text\">a_price = weight assigned to price (USD)\na_room  = weight assigned to number of rooms\na_lot   = weight assigned to lot size (sq.ft.)</code></co-content>"
#                   }
#                 },
#                 "options": [
#                   {
#                     "id": "0.9109180361318947",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1, a_room = 1, a_lot = 1</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.11974743029080992",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1, a_room = 1, a_lot = 1e-6</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.8214165539451299",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e-10, a_room = 1, a_lot = 1e-6</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.6784789645868041",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e-5, a_room = 1, a_lot = 1e-3</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.9664001374497642",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>a_price = 1e5, a_room = 1, a_lot = 1e3</text></co-content>"
#                       }
#                     }
#                   }
#                 ]
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "jeVDBjnNEeaetxLgjw7H8Q@0",
#             "question": {
#               "type": "singleNumeric"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nConsider the following two sentences.\n</text><list bulletType=\"bullets\"><li><text>Sentence 1: The quick brown fox jumps over the lazy dog.\n</text></li><li><text>Sentence 2: A quick brown dog outpaces a quick fox.\n</text></li></list><text>\n\nCompute the Euclidean distance using word counts. Round your answer to 3 decimal places.</text><text>Note. To compute word counts, turn all words into lower case and strip all punctuation, so that \"The\" and \"the\" are counted as the same token.</text></co-content>"
#                   }
#                 }
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "-tI-EjnNEeaPCw5NUSdt1w@0",
#             "question": {
#               "type": "singleNumeric"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>Refer back to the two sentences given in Question 2 to answer the following:</text><text>Recall that we can use cosine similarity to define a distance.  We call that distance cosine distance. </text><text>Compute the <strong>cosine distance</strong> using word counts. Round your answer to 3 decimal places.\n</text><text>Note: To compute word counts, turn all words into lower case and strip all punctuation, so that \"The\" and \"the\" are counted as the same token.</text><text>Hint. Recall that we can use cosine similarity to define a distance.  We call that distance cosine distance.</text></co-content>"
#                   }
#                 }
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "LGECRDnOEeaetxLgjw7H8Q@0",
#             "question": {
#               "type": "mcq"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>(True/False) For positive features, cosine similarity is always between 0 and 1.</text></co-content>"
#                   }
#                 },
#                 "options": [
#                   {
#                     "id": "0.838238929639803",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>True</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.9654190569725087",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>False</text></co-content>"
#                       }
#                     }
#                   }
#                 ]
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "N62eSDnOEea5PAq35BZMoQ@0",
#             "question": {
#               "type": "mcq"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nUsing the formula for TF-IDF presented in the lecture, complete the following sentence:</text><text>A word is assigned a zero TF-IDF weight when it appears in ____ documents. (N: number of documents in the corpus)</text></co-content>"
#                   }
#                 },
#                 "options": [
#                   {
#                     "id": "0.10877084920366831",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>N - 1</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.29922629273211787",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>N/2</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.69796593807345",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>N</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.6731572688278926",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>0.1*N</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.8467992755507772",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>100</text></co-content>"
#                       }
#                     }
#                   }
#                 ]
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           },
#           {
#             "id": "TuHdkjnOEeaPCw5NUSdt1w@0",
#             "question": {
#               "type": "mcq"
#             },
#             "variant": {
#               "definition": {
#                 "prompt": {
#                   "typeName": "cml",
#                   "definition": {
#                     "dtdId": "assess/1",
#                     "value": "<co-content><text>\n\nWhich of the following does <strong>not </strong>describe the word count document representation?</text></co-content>"
#                   }
#                 },
#                 "options": [
#                   {
#                     "id": "0.3821039264467949",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>Ignores the order of the words</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.3470767421220087",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>Assigns a high score to a frequently occurring word</text></co-content>"
#                       }
#                     }
#                   },
#                   {
#                     "id": "0.3341840649172314",
#                     "display": {
#                       "typeName": "cml",
#                       "definition": {
#                         "dtdId": "assess/1",
#                         "value": "<co-content><text>Penalizes words that appear in every document</text></co-content>"
#                       }
#                     }
#                   }
#                 ]
#               },
#               "detailLevel": "Full"
#             },
#             "weightedScoring": {
#               "maxScore": 1
#             },
#             "isSubmitAllowed": true
#           }
#         ],
#         "evaluation": null
#       }
#     }
#   ],
#   "paging": null,
#   "linked": {
#     "gradingAttempts.v1": []
#   }
# }
#
# Request payload:
# {"name":"getState","argument":[]}
POST_OPENCOURSE_ONDEMAND_EXAM_SESSIONS_GET_STATE = 'https://www.coursera.org/api/onDemandExamSessions.v1/{session_id}/actions?includes=gradingAttempts'

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
# define a per-user cache folder
if os.name == "posix":  # pragma: no cover
    import pwd
    _USER = pwd.getpwuid(os.getuid())[0]
else:
    _USER = getpass.getuser()

PATH_CACHE = os.path.join(tempfile.gettempdir(), _USER + "_coursera_dl_cache")
PATH_COOKIES = os.path.join(PATH_CACHE, 'cookies')

WINDOWS_UNC_PREFIX = u'\\\\?\\'

#: This extension is used to save contents of supplementary instructions.
IN_MEMORY_EXTENSION = 'html'

#: This marker is added in front of a URL when supplementary instructions
#: are passed from parser to downloader. URL field fill contain the data
#: that will be stored to a file. The marker should be removed from URL
#: field first.
IN_MEMORY_MARKER = '#inmemory#'

#: These are hard limits for format (file extension) and
#: title (file name) lengths to avoid too long file names
#: (longer than 255 characters)
FORMAT_MAX_LENGTH = 20
TITLE_MAX_LENGTH = 200

#: CSS that is usen to prettify instructions
INSTRUCTIONS_HTML_INJECTION = '''
<style>
body {
    padding: 50px 85px 50px 85px;
}

table th, table td {
    border: 1px solid #e0e0e0;
    padding: 5px 20px;
    text-align: left;
}
input {
    margin: 10px;
}
}
th {
    font-weight: bold;
}
td, th {
    display: table-cell;
    vertical-align: inherit;
}
img {
    height: auto;
    max-width: 100%;
}
pre {
    display: block;
    margin: 20px;
    background: #424242;
    color: #fff;
    font-size: 13px;
    white-space: pre-wrap;
    padding: 9.5px;
    margin: 0 0 10px;
    border: 1px solid #ccc;
}
</style>

<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

<script type="text/x-mathjax-config">
  MathJax.Hub.Config({
    tex2jax: {
      inlineMath: [ ['$$','$$'], ['$','$'] ],
      displayMath: [ ["\\\\[","\\\\]"] ],
      processEscapes: true
    }
  });
</script>
'''
