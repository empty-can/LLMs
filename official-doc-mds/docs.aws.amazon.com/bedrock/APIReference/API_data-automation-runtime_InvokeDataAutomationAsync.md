

# InvokeDataAutomationAsync
<a name="API_data-automation-runtime_InvokeDataAutomationAsync"></a>

Process data with a data automation project or blueprints. The service processes data asynchronously and stores the output in the S3 bucket that you specify. To check if an invocation is complete, use [GetDataAutomationStatus](API_data-automation-runtime_GetDataAutomationStatus.md).

## Request Syntax
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax"></a>

```
{
   "blueprints": [ 
      { 
         "blueprintArn": "{{string}}",
         "stage": "{{string}}",
         "version": "{{string}}"
      }
   ],
   "clientToken": "{{string}}",
   "dataAutomationConfiguration": { 
      "dataAutomationProjectArn": "{{string}}",
      "stage": "{{string}}"
   },
   "dataAutomationProfileArn": "{{string}}",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "inputConfiguration": { 
      "assetProcessingConfiguration": { 
         "video": { 
            "segmentConfiguration": { ... }
         }
      },
      "s3Uri": "{{string}}"
   },
   "notificationConfiguration": { 
      "eventBridgeConfiguration": { 
         "eventBridgeEnabled": {{boolean}}
      }
   },
   "outputConfiguration": { 
      "s3Uri": "{{string}}"
   },
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [blueprints](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-blueprints"></a>
A list of blueprints to apply to the data.  
Type: Array of [Blueprint](API_data-automation-runtime_Blueprint.md) objects  
Array Members: Minimum number of 1 item. Maximum number of 40 items.  
Required: No

 ** [clientToken](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-clientToken"></a>
To avoid making duplicate calls, specify a unique token for this invocation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9])*`   
Required: No

 ** [dataAutomationConfiguration](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-dataAutomationConfiguration"></a>
The data automation project to process the data with.  
Type: [DataAutomationConfiguration](API_data-automation-runtime_DataAutomationConfiguration.md) object  
Required: No

 ** [dataAutomationProfileArn](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-dataAutomationProfileArn"></a>
The ARN of the profile calling your request.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:(aws|[0-9]{12}):data-automation-profile/[a-zA-Z0-9-_.]+`   
Required: Yes

 ** [encryptionConfiguration](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-encryptionConfiguration"></a>
Encryption settings for the invocation.  
Type: [EncryptionConfiguration](API_data-automation-runtime_EncryptionConfiguration.md) object  
Required: No

 ** [inputConfiguration](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-inputConfiguration"></a>
Where to read the input data from.  
Type: [InputConfiguration](API_data-automation-runtime_InputConfiguration.md) object  
Required: Yes

 ** [notificationConfiguration](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-notificationConfiguration"></a>
Notification settings for the invocation.  
Type: [NotificationConfiguration](API_data-automation-runtime_NotificationConfiguration.md) object  
Required: No

 ** [outputConfiguration](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-outputConfiguration"></a>
Where to store the output.  
Type: [OutputConfiguration](API_data-automation-runtime_OutputConfiguration.md) object  
Required: Yes

 ** [tags](#API_data-automation-runtime_InvokeDataAutomationAsync_RequestSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-request-tags"></a>
Tags associated with your inference at time of creation.  
Type: Array of [Tag](API_data-automation-runtime_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_ResponseSyntax"></a>

```
{
   "invocationArn": "string"
}
```

## Response Elements
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [invocationArn](#API_data-automation-runtime_InvokeDataAutomationAsync_ResponseSyntax) **   <a name="bedrock-data-automation-runtime_InvokeDataAutomationAsync-response-invocationArn"></a>
The ARN of the invocation.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:(insights-invocation|data-automation-invocation)/[a-zA-Z0-9-_]+` 

## Errors
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
  
HTTP Status Code: 400

 ** InternalServerException **   
  
HTTP Status Code: 500

 ** ServiceQuotaExceededException **   
  
HTTP Status Code: 400

 ** ThrottlingException **   
  
HTTP Status Code: 400

 ** ValidationException **   
  
HTTP Status Code: 400

## See Also
<a name="API_data-automation-runtime_InvokeDataAutomationAsync_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-runtime-2024-06-13/InvokeDataAutomationAsync) 