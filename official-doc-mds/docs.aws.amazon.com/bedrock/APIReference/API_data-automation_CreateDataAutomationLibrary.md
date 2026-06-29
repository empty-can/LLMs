

# CreateDataAutomationLibrary
<a name="API_data-automation_CreateDataAutomationLibrary"></a>

Creates a data automation library.

## Request Syntax
<a name="API_data-automation_CreateDataAutomationLibrary_RequestSyntax"></a>

```
PUT /data-automation-libraries/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "encryptionConfiguration": { 
      "kmsEncryptionContext": { 
         "{{string}}" : "{{string}}" 
      },
      "kmsKeyId": "{{string}}"
   },
   "libraryDescription": "{{string}}",
   "libraryName": "{{string}}",
   "tags": [ 
      { 
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_data-automation_CreateDataAutomationLibrary_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_data-automation_CreateDataAutomationLibrary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_data-automation_CreateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-request-clientToken"></a>
To avoid creating duplicate resources, specify a unique token for this library.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [encryptionConfiguration](#API_data-automation_CreateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-request-encryptionConfiguration"></a>
Encryption settings for the library.  
Type: [EncryptionConfiguration](API_data-automation_EncryptionConfiguration.md) object  
Required: No

 ** [libraryDescription](#API_data-automation_CreateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-request-libraryDescription"></a>
A description for the library.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Pattern: `[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*`   
Required: No

 ** [libraryName](#API_data-automation_CreateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-request-libraryName"></a>
A name for the library.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 128.  
Pattern: `[a-zA-Z0-9-_]+`   
Required: Yes

 ** [tags](#API_data-automation_CreateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-request-tags"></a>
Tags assigned to the library at time of creation.  
Type: Array of [Tag](API_data-automation_Tag.md) objects  
Array Members: Minimum number of 0 items. Maximum number of 200 items.  
Required: No

## Response Syntax
<a name="API_data-automation_CreateDataAutomationLibrary_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "libraryArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_CreateDataAutomationLibrary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [libraryArn](#API_data-automation_CreateDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-response-libraryArn"></a>
The library's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}` 

 ** [status](#API_data-automation_CreateDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_CreateDataAutomationLibrary-response-status"></a>
The library's status.  
Type: String  
Valid Values: `ACTIVE | DELETING` 

## Errors
<a name="API_data-automation_CreateDataAutomationLibrary_Errors"></a>

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
<a name="API_data-automation_CreateDataAutomationLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/CreateDataAutomationLibrary) 