

# UpdateDataAutomationLibrary
<a name="API_data-automation_UpdateDataAutomationLibrary"></a>

Updates a data automation library.

## Request Syntax
<a name="API_data-automation_UpdateDataAutomationLibrary_RequestSyntax"></a>

```
PUT /data-automation-libraries/{{libraryArn}}/ HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "libraryDescription": "{{string}}"
}
```

## URI Request Parameters
<a name="API_data-automation_UpdateDataAutomationLibrary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [libraryArn](#API_data-automation_UpdateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_UpdateDataAutomationLibrary-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_UpdateDataAutomationLibrary_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_data-automation_UpdateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_UpdateDataAutomationLibrary-request-clientToken"></a>
To avoid creating duplicate resources, specify a unique token for this operation.  
Type: String  
Length Constraints: Minimum length of 33. Maximum length of 256.  
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`   
Required: No

 ** [libraryDescription](#API_data-automation_UpdateDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_UpdateDataAutomationLibrary-request-libraryDescription"></a>
A description for the library.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 300.  
Pattern: `[a-zA-Z0-9\s!"\#\$%'&\(\)\*\+\,\-\./:;=\?@\[\\\]\^_`\{\|\}~><À-ÖØ-Üßà-öø-üẞ¿¡Œ-œ°£¥₹€§©ª®™¹±-µ✓⑆-⑉฿₽₱₦₣₩₫₺]*`   
Required: No

## Response Syntax
<a name="API_data-automation_UpdateDataAutomationLibrary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "libraryArn": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_data-automation_UpdateDataAutomationLibrary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [libraryArn](#API_data-automation_UpdateDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_UpdateDataAutomationLibrary-response-libraryArn"></a>
The library's ARN.  
Type: String  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}` 

 ** [status](#API_data-automation_UpdateDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_UpdateDataAutomationLibrary-response-status"></a>
The library's status.  
Type: String  
Valid Values: `ACTIVE | DELETING` 

## Errors
<a name="API_data-automation_UpdateDataAutomationLibrary_Errors"></a>

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
<a name="API_data-automation_UpdateDataAutomationLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/UpdateDataAutomationLibrary) 