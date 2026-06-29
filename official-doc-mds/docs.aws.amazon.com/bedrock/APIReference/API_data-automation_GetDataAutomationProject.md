

# GetDataAutomationProject
<a name="API_data-automation_GetDataAutomationProject"></a>

Gets details about a data automation project.

## Request Syntax
<a name="API_data-automation_GetDataAutomationProject_RequestSyntax"></a>

```
POST /data-automation-projects/{{projectArn}}/ HTTP/1.1
Content-type: application/json

{
   "projectStage": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_GetDataAutomationProject_RequestParameters"></a>

The request uses the following URI parameters.

 ** [projectArn](#API_data-automation_GetDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationProject-request-uri-projectArn"></a>
The project's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_GetDataAutomationProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [projectStage](#API_data-automation_GetDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationProject-request-projectStage"></a>
To view the development stage, set to `DEVELOPMENT`.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

## Response Syntax
<a name="API_data-automation_GetDataAutomationProject_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "project": { 
      "creationTime": "string",
      "customOutputConfiguration": { 
         "blueprints": [ 
            { 
               "blueprintArn": "string",
               "blueprintStage": "string",
               "blueprintVersion": "string"
            }
         ],
         "document": { 
            "fallbackBlueprints": [ 
               { 
                  "blueprintArn": "string",
                  "blueprintStage": "string",
                  "blueprintVersion": "string"
               }
            ]
         }
      },
      "dataAutomationLibraryConfiguration": { 
         "libraries": [ 
            { 
               "libraryArn": "string"
            }
         ]
      },
      "kmsEncryptionContext": { 
         "string" : "string" 
      },
      "kmsKeyId": "string",
      "lastModifiedTime": "string",
      "overrideConfiguration": { 
         "audio": { 
            "languageConfiguration": { 
               "generativeOutputLanguage": "string",
               "identifyMultipleLanguages": boolean,
               "inputLanguages": [ "string" ]
            },
            "modalityProcessing": { 
               "state": "string"
            },
            "sensitiveDataConfiguration": { 
               "detectionMode": "string",
               "detectionScope": [ "string" ],
               "piiEntitiesConfiguration": { 
                  "piiEntityTypes": [ "string" ],
                  "redactionMaskMode": "string"
               }
            }
         },
         "document": { 
            "modalityProcessing": { 
               "state": "string"
            },
            "sensitiveDataConfiguration": { 
               "detectionMode": "string",
               "detectionScope": [ "string" ],
               "piiEntitiesConfiguration": { 
                  "piiEntityTypes": [ "string" ],
                  "redactionMaskMode": "string"
               }
            },
            "splitter": { 
               "state": "string"
            }
         },
         "image": { 
            "modalityProcessing": { 
               "state": "string"
            },
            "sensitiveDataConfiguration": { 
               "detectionMode": "string",
               "detectionScope": [ "string" ],
               "piiEntitiesConfiguration": { 
                  "piiEntityTypes": [ "string" ],
                  "redactionMaskMode": "string"
               }
            }
         },
         "modalityRouting": { 
            "jpeg": "string",
            "mov": "string",
            "mp4": "string",
            "png": "string"
         },
         "video": { 
            "modalityProcessing": { 
               "state": "string"
            },
            "sensitiveDataConfiguration": { 
               "detectionMode": "string",
               "detectionScope": [ "string" ],
               "piiEntitiesConfiguration": { 
                  "piiEntityTypes": [ "string" ],
                  "redactionMaskMode": "string"
               }
            }
         }
      },
      "projectArn": "string",
      "projectDescription": "string",
      "projectName": "string",
      "projectStage": "string",
      "projectType": "string",
      "standardOutputConfiguration": { 
         "audio": { 
            "extraction": { 
               "category": { 
                  "state": "string",
                  "typeConfiguration": { 
                     "transcript": { 
                        "channelLabeling": { 
                           "state": "string"
                        },
                        "speakerLabeling": { 
                           "state": "string"
                        }
                     }
                  },
                  "types": [ "string" ]
               }
            },
            "generativeField": { 
               "state": "string",
               "types": [ "string" ]
            }
         },
         "document": { 
            "extraction": { 
               "boundingBox": { 
                  "state": "string"
               },
               "granularity": { 
                  "types": [ "string" ]
               }
            },
            "generativeField": { 
               "state": "string"
            },
            "outputFormat": { 
               "additionalFileFormat": { 
                  "state": "string"
               },
               "textFormat": { 
                  "types": [ "string" ]
               }
            }
         },
         "image": { 
            "extraction": { 
               "boundingBox": { 
                  "state": "string"
               },
               "category": { 
                  "state": "string",
                  "types": [ "string" ]
               }
            },
            "generativeField": { 
               "state": "string",
               "types": [ "string" ]
            }
         },
         "video": { 
            "extraction": { 
               "boundingBox": { 
                  "state": "string"
               },
               "category": { 
                  "state": "string",
                  "types": [ "string" ]
               }
            },
            "generativeField": { 
               "state": "string",
               "types": [ "string" ]
            }
         }
      },
      "status": "string"
   }
}
```

## Response Elements
<a name="API_data-automation_GetDataAutomationProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [project](#API_data-automation_GetDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_GetDataAutomationProject-response-project"></a>
Details about the project.  
Type: [DataAutomationProject](API_data-automation_DataAutomationProject.md) object

## Errors
<a name="API_data-automation_GetDataAutomationProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_GetDataAutomationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/GetDataAutomationProject) 