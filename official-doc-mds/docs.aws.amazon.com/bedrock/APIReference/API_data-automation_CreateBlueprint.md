

# CreateBlueprint
<a name="API_data-automation_CreateBlueprint"></a>

Creates a blueprint. A blueprint has a schema that maps data fields to prompts that tell a model how to get the data out of an image or document. For schema examples, use [ListBlueprints](API_data-automation_ListBlueprints.md) to get a list of public blueprints and [GetBlueprint](API_data-automation_GetBlueprint.md) to view a blueprint.

## Request Syntax
<a name="API_data-automation_CreateBlueprint_RequestSyntax"></a>

```
PUT /blueprints/ HTTP/1.1
Content-type: application/json

{
   "blueprintName": "{{string}}",
   "blueprintStage": "{{string}}",
   "clientToken": "{{string}}",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "schema": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_CreateBlueprint_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_CreateBlueprint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprintName](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-blueprintName"></a>
A name for the blueprint.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** [blueprintStage](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-blueprintStage"></a>
To indicate that the blueprint is not final, set to `DEVELOPMENT`. Otherwise, the blueprint is created in the `LIVE` stage.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** [clientToken](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-clientToken"></a>
To avoid creating duplicate resources, specify a unique token for this blueprint.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [encryptionConfiguration](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-encryptionConfiguration"></a>
Encryption settings for the blueprint.  
Type: [EncryptionConfiguration](API_data-automation_EncryptionConfiguration.md) object  
Required: No

 ** [schema](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-schema"></a>
The blueprint's schema.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: Yes

 ** [tags](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-tags"></a>
Tags assigned to a blueprint at time of creation.  
Type: Array of [Tag](API_data-automation_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

 ** [type](#API_data-automation_CreateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-request-type"></a>
The type of blueprint to create.  
Type: String  
Valid Values: `DOCUMENT | IMAGE | AUDIO`   
Required: Yes

## Response Syntax
<a name="API_data-automation_CreateBlueprint_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "blueprint": { 
      "blueprintArn": "string",
      "blueprintName": "string",
      "blueprintStage": "string",
      "blueprintVersion": "string",
      "creationTime": "string",
      "kmsEncryptionContext": { 
         "string" : "string" 
      },
      "kmsKeyId": "string",
      "lastModifiedTime": "string",
      "optimizationSamples": [ 
         { 
            "assetS3Object": { 
               "s3Uri": "string",
               "version": "string"
            },
            "groundTruthS3Object": { 
               "s3Uri": "string",
               "version": "string"
            }
         }
      ],
      "optimizationTime": "string",
      "schema": "string",
      "type": "string"
   }
}
```

## Response Elements
<a name="API_data-automation_CreateBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [blueprint](#API_data-automation_CreateBlueprint_ResponseSyntax) **   <a name="bedrock-data-automation_CreateBlueprint-response-blueprint"></a>
Details about the blueprint.  
Type: [Blueprint](API_data-automation_Blueprint.md) object

## Errors
<a name="API_data-automation_CreateBlueprint_Errors"></a>

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
<a name="API_data-automation_CreateBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/CreateBlueprint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/CreateBlueprint) 