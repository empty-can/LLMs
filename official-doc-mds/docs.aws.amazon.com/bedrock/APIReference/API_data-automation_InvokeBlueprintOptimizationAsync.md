

# InvokeBlueprintOptimizationAsync
<a name="API_data-automation_InvokeBlueprintOptimizationAsync"></a>

Starts an asynchronous job to optimize a blueprint using sample data.

## Request Syntax
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax"></a>

```
POST /invokeBlueprintOptimizationAsync HTTP/1.1
Content-type: application/json

{
   "blueprint": { 
      "blueprintArn": "{{string}}",
      "stage": "{{string}}"
   },
   "dataAutomationProfileArn": "{{string}}",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "outputConfiguration": { 
      "s3Object": { 
         "s3Uri": "{{string}}",
         "version": "{{string}}"
      }
   },
   "samples": [ 
      { 
         "assetS3Object": { 
            "s3Uri": "{{string}}",
            "version": "{{string}}"
         },
         "groundTruthS3Object": { 
            "s3Uri": "{{string}}",
            "version": "{{string}}"
         }
      }
   ],
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [blueprint](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-blueprint"></a>
The blueprint to optimize.  
Type: [BlueprintOptimizationObject](API_data-automation_BlueprintOptimizationObject.md) object  
Required: Yes

 ** [dataAutomationProfileArn](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-dataAutomationProfileArn"></a>
The ARN of the data automation profile to use.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-profile/[a-zA-Z0-9-_.]+`   
Required: Yes

 ** [encryptionConfiguration](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-encryptionConfiguration"></a>
Encryption settings for the optimization job.  
Type: [EncryptionConfiguration](API_data-automation_EncryptionConfiguration.md) object  
Required: No

 ** [outputConfiguration](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-outputConfiguration"></a>
Where to store the optimization results.  
Type: [BlueprintOptimizationOutputConfiguration](API_data-automation_BlueprintOptimizationOutputConfiguration.md) object  
Required: Yes

 ** [samples](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-samples"></a>
Sample assets and ground truth data to use for optimization.  
Type: Array of [BlueprintOptimizationSample](API_data-automation_BlueprintOptimizationSample.md) objects  
Required: Yes

 ** [tags](#API_data-automation_InvokeBlueprintOptimizationAsync_RequestSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-request-tags"></a>
Tags to assign to the optimization job.  
Type: Array of [Tag](API_data-automation_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "invocationArn": "string"
}
```

## Response Elements
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationArn](#API_data-automation_InvokeBlueprintOptimizationAsync_ResponseSyntax) **   <a name="bedrock-data-automation_InvokeBlueprintOptimizationAsync-response-invocationArn"></a>
The ARN of the optimization job invocation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:blueprint-optimization-invocation/[a-zA-Z0-9-_]+` 

## Errors
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 403

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ResourceNotFoundException **   
  
HTTP Status Code: 404

 ** ServiceQuotaExceededException **   
  
HTTP Status Code: 402

 ** ThrottlingException **   
  
HTTP Status Code: 429

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation_InvokeBlueprintOptimizationAsync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/InvokeBlueprintOptimizationAsync) 