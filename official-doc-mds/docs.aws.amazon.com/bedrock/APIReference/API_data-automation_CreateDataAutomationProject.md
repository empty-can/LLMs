

# CreateDataAutomationProject
<a name="API_data-automation_CreateDataAutomationProject"></a>

Creates a data automation project.

## Request Syntax
<a name="API_data-automation_CreateDataAutomationProject_RequestSyntax"></a>

```
PUT /data-automation-projects/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "customOutputConfiguration": { 
      "blueprints": [ 
         { 
            "blueprintArn": "{{string}}",
            "blueprintStage": "{{string}}",
            "blueprintVersion": "{{string}}"
         }
      ],
      "document": { 
         "fallbackBlueprints": [ 
            { 
               "blueprintArn": "{{string}}",
               "blueprintStage": "{{string}}",
               "blueprintVersion": "{{string}}"
            }
         ]
      }
   },
   "dataAutomationLibraryConfiguration": { 
      "libraries": [ 
         { 
            "libraryArn": "{{string}}"
         }
      ]
   },
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "overrideConfiguration": { 
      "audio": { 
         "languageConfiguration": { 
            "generativeOutputLanguage": "{{string}}",
            "identifyMultipleLanguages": {{boolean}},
            "inputLanguages": [ "{{string}}" ]
         },
         "modalityProcessing": { 
            "state": "{{string}}"
         },
         "sensitiveDataConfiguration": { 
            "detectionMode": "{{string}}",
            "detectionScope": [ "{{string}}" ],
            "piiEntitiesConfiguration": { 
               "piiEntityTypes": [ "{{string}}" ],
               "redactionMaskMode": "{{string}}"
            }
         }
      },
      "document": { 
         "modalityProcessing": { 
            "state": "{{string}}"
         },
         "sensitiveDataConfiguration": { 
            "detectionMode": "{{string}}",
            "detectionScope": [ "{{string}}" ],
            "piiEntitiesConfiguration": { 
               "piiEntityTypes": [ "{{string}}" ],
               "redactionMaskMode": "{{string}}"
            }
         },
         "splitter": { 
            "state": "{{string}}"
         }
      },
      "image": { 
         "modalityProcessing": { 
            "state": "{{string}}"
         },
         "sensitiveDataConfiguration": { 
            "detectionMode": "{{string}}",
            "detectionScope": [ "{{string}}" ],
            "piiEntitiesConfiguration": { 
               "piiEntityTypes": [ "{{string}}" ],
               "redactionMaskMode": "{{string}}"
            }
         }
      },
      "modalityRouting": { 
         "jpeg": "{{string}}",
         "mov": "{{string}}",
         "mp4": "{{string}}",
         "png": "{{string}}"
      },
      "video": { 
         "modalityProcessing": { 
            "state": "{{string}}"
         },
         "sensitiveDataConfiguration": { 
            "detectionMode": "{{string}}",
            "detectionScope": [ "{{string}}" ],
            "piiEntitiesConfiguration": { 
               "piiEntityTypes": [ "{{string}}" ],
               "redactionMaskMode": "{{string}}"
            }
         }
      }
   },
   "projectDescription": "{{string}}",
   "projectName": "{{string}}",
   "projectStage": "{{string}}",
   "projectType": "{{string}}",
   "standardOutputConfiguration": { 
      "audio": { 
         "extraction": { 
            "category": { 
               "state": "{{string}}",
               "typeConfiguration": { 
                  "transcript": { 
                     "channelLabeling": { 
                        "state": "{{string}}"
                     },
                     "speakerLabeling": { 
                        "state": "{{string}}"
                     }
                  }
               },
               "types": [ "{{string}}" ]
            }
         },
         "generativeField": { 
            "state": "{{string}}",
            "types": [ "{{string}}" ]
         }
      },
      "document": { 
         "extraction": { 
            "boundingBox": { 
               "state": "{{string}}"
            },
            "granularity": { 
               "types": [ "{{string}}" ]
            }
         },
         "generativeField": { 
            "state": "{{string}}"
         },
         "outputFormat": { 
            "additionalFileFormat": { 
               "state": "{{string}}"
            },
            "textFormat": { 
               "types": [ "{{string}}" ]
            }
         }
      },
      "image": { 
         "extraction": { 
            "boundingBox": { 
               "state": "{{string}}"
            },
            "category": { 
               "state": "{{string}}",
               "types": [ "{{string}}" ]
            }
         },
         "generativeField": { 
            "state": "{{string}}",
            "types": [ "{{string}}" ]
         }
      },
      "video": { 
         "extraction": { 
            "boundingBox": { 
               "state": "{{string}}"
            },
            "category": { 
               "state": "{{string}}",
               "types": [ "{{string}}" ]
            }
         },
         "generativeField": { 
            "state": "{{string}}",
            "types": [ "{{string}}" ]
         }
      }
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_data-automation_CreateDataAutomationProject_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_CreateDataAutomationProject_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-clientToken"></a>
To avoid creating duplicate resources, specify a unique token for this project.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [customOutputConfiguration](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-customOutputConfiguration"></a>
Blueprints to enabled for the project.  
Type: [CustomOutputConfiguration](API_data-automation_CustomOutputConfiguration.md) object  
Required: No

 ** [dataAutomationLibraryConfiguration](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-dataAutomationLibraryConfiguration"></a>
Library configuration for the project.  
Type: [DataAutomationLibraryConfiguration](API_data-automation_DataAutomationLibraryConfiguration.md) object  
Required: No

 ** [encryptionConfiguration](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-encryptionConfiguration"></a>
Encryption settings for the project.  
Type: [EncryptionConfiguration](API_data-automation_EncryptionConfiguration.md) object  
Required: No

 ** [overrideConfiguration](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-overrideConfiguration"></a>
Additional settings to apply to the project.  
Type: [OverrideConfiguration](API_data-automation_OverrideConfiguration.md) object  
Required: No

 ** [projectDescription](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-projectDescription"></a>
A description for the project.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Required: No

 ** [projectName](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-projectName"></a>
A name for the project.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** [projectStage](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-projectStage"></a>
To indicate that the project is not final, set to `DEVELOPMENT`. Otherwise, the project is created in the `LIVE` stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** [projectType](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-projectType"></a>
The type of bedrock data automation API that is compatible with this project.  
Type: String  
Valid Values: `ASYNC | SYNC`   
Required: No

 ** [standardOutputConfiguration](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-standardOutputConfiguration"></a>
The standard output configuration for the project. If you omit settings for any types, default settings are applied. You can specify an empty configuration to create a project with default settings and view the settings with [GetDataAutomationProject](API_data-automation_GetDataAutomationProject.md).  
Type: [StandardOutputConfiguration](API_data-automation_StandardOutputConfiguration.md) object  
Required: Yes

 ** [tags](#API_data-automation_CreateDataAutomationProject_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-request-tags"></a>
Tags assigned to the project at time of creation.  
Type: Array of [Tag](API_data-automation_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_data-automation_CreateDataAutomationProject_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "projectArn": "string",
   "projectStage": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_CreateDataAutomationProject_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [projectArn](#API_data-automation_CreateDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-response-projectArn"></a>
The project's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-project/[a-zA-Z0-9-]{12,36}` 

 ** [projectStage](#API_data-automation_CreateDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-response-projectStage"></a>
The project's stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE` 

 ** [status](#API_data-automation_CreateDataAutomationProject_ResponseSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationProject-response-status"></a>
The project's status.  
Type: String  
Valid Values: `COMPLETED | IN_PROGRESS | FAILED` 

## Errors
<a name="API_data-automation_CreateDataAutomationProject_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** ConflictException **   
  
HTTP Status Code: 409

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
  
HTTP Status Code: 402

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_CreateDataAutomationProject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/CreateDataAutomationProject) 