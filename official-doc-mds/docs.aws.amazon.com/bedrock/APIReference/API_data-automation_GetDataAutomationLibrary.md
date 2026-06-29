

# GetDataAutomationLibrary
<a name="API_data-automation_GetDataAutomationLibrary"></a>

Gets details about a data automation library.

## Request Syntax
<a name="API_data-automation_GetDataAutomationLibrary_RequestSyntax"></a>

```
POST /data-automation-libraries/{{libraryArn}}/ HTTP/1.1
```

## URI Request Parameters
<a name="API_data-automation_GetDataAutomationLibrary_RequestParameters"></a>

The request uses the following URI parameters.

 ** [libraryArn](#API_data-automation_GetDataAutomationLibrary_RequestSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibrary-request-uri-libraryArn"></a>
The library's ARN.  
Length Constraints: Minimum length of 0. Maximum length of 128.  
Pattern: `arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):bedrock:[a-zA-Z0-9-]*:[0-9]{12}:data-automation-library/[a-zA-Z0-9-]{12,36}`   
Required: Yes

## Request Body
<a name="API_data-automation_GetDataAutomationLibrary_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_data-automation_GetDataAutomationLibrary_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "library": { 
      "creationTime": "string",
      "entityTypes": [ 
         { 
            "entityMetadata": "string",
            "entityType": "string"
         }
      ],
      "kmsEncryptionContext": { 
         "string" : "string" 
      },
      "kmsKeyId": "string",
      "libraryArn": "string",
      "libraryDescription": "string",
      "libraryName": "string",
      "status": "string"
   }
}
```

## Response Elements
<a name="API_data-automation_GetDataAutomationLibrary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [library](#API_data-automation_GetDataAutomationLibrary_ResponseSyntax) **   <a name="bedrock-data-automation_GetDataAutomationLibrary-response-library"></a>
Details about the library.  
Type: [DataAutomationLibrary](API_data-automation_DataAutomationLibrary.md) object

## Errors
<a name="API_data-automation_GetDataAutomationLibrary_Errors"></a>

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
<a name="API_data-automation_GetDataAutomationLibrary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-data-automation-2023-07-26/GetDataAutomationLibrary) 