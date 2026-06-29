

# UpdateBlueprint
<a name="API_data-automation_UpdateBlueprint"></a>

Updates a blueprint.

## Request Syntax
<a name="API_data-automation_UpdateBlueprint_RequestSyntax"></a>

```
PUT /blueprints/{{blueprintArn}}/ HTTP/1.1
Content-type: application/json

{
   "blueprintStage": "{{string}}",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "schema": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_UpdateBlueprint_RequestParameters"></a>

The request uses the following URI parameters.

 ** [blueprintArn](#API_data-automation_UpdateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_UpdateBlueprint-request-uri-blueprintArn"></a>
The blueprint's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(bedrock-data-automation-public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})`   
Required: Yes

## Request Body
<a name="API_data-automation_UpdateBlueprint_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprintStage](#API_data-automation_UpdateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_UpdateBlueprint-request-blueprintStage"></a>
To update the development stage, set to `DEVELOPMENT`.  
Type: String  
Valid Values: `DEVELOPMENT | LIVE`   
Required: No

 ** [encryptionConfiguration](#API_data-automation_UpdateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_UpdateBlueprint-request-encryptionConfiguration"></a>
Encryption for the updated blueprint.  
Type: [EncryptionConfiguration](API_data-automation_EncryptionConfiguration.md) object  
Required: No

 ** [schema](#API_data-automation_UpdateBlueprint_RequestSyntax) **   <a name="bedrock-data-automation_UpdateBlueprint-request-schema"></a>
The blueprint's schema.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 100000.  
Required: Yes

## Response Syntax
<a name="API_data-automation_UpdateBlueprint_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_data-automation_UpdateBlueprint_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blueprint](#API_data-automation_UpdateBlueprint_ResponseSyntax) **   <a name="bedrock-data-automation_UpdateBlueprint-response-blueprint"></a>
Details about the blueprint.  
Type: [Blueprint](API_data-automation_Blueprint.md) object

## Errors
<a name="API_data-automation_UpdateBlueprint_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** ConflictException **   
  
HTTP Status Code: 409

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_UpdateBlueprint_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/UpdateBlueprint) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/UpdateBlueprint) 