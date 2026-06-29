

# ListAsyncInvokes
<a name="API_runtime_ListAsyncInvokes"></a>

Lists asynchronous invocations.

## Request Syntax
<a name="API_runtime_ListAsyncInvokes_RequestSyntax"></a>

```
GET /async-invoke?maxResults={{maxResults}}&nextToken={{nextToken}}&sortBy={{sortBy}}&sortOrder={{sortOrder}}&statusEquals={{statusEquals}}&submitTimeAfter={{submitTimeAfter}}&submitTimeBefore={{submitTimeBefore}} HTTP/1.1
```

## URI Request Parameters
<a name="API_runtime_ListAsyncInvokes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-maxResults"></a>
The maximum number of invocations to return in one page of results.  
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

 ** [sortBy](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-sortBy"></a>
How to sort the response.  
Valid Values: `SubmissionTime` 

 ** [sortOrder](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-sortOrder"></a>
The sorting order for the response.  
Valid Values: `Ascending | Descending` 

 ** [statusEquals](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-statusEquals"></a>
Filter invocations by status.  
Valid Values: `InProgress | Completed | Failed` 

 ** [submitTimeAfter](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-submitTimeAfter"></a>
Include invocations submitted after this time.

 ** [submitTimeBefore](#API_runtime_ListAsyncInvokes_RequestSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-request-uri-submitTimeBefore"></a>
Include invocations submitted before this time.

## Request Body
<a name="API_runtime_ListAsyncInvokes_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_runtime_ListAsyncInvokes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "asyncInvokeSummaries": [ 
      { 
         "clientRequestToken": "string",
         "endTime": "string",
         "failureMessage": "string",
         "invocationArn": "string",
         "lastModifiedTime": "string",
         "modelArn": "string",
         "outputDataConfig": { ... },
         "status": "string",
         "submitTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_runtime_ListAsyncInvokes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [asyncInvokeSummaries](#API_runtime_ListAsyncInvokes_ResponseSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-response-asyncInvokeSummaries"></a>
A list of invocation summaries.  
Type: Array of [AsyncInvokeSummary](API_runtime_AsyncInvokeSummary.md) objects

 ** [nextToken](#API_runtime_ListAsyncInvokes_ResponseSyntax) **   <a name="bedrock-runtime_ListAsyncInvokes-response-nextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.  
Type: String  
Length Constraints: Minimum length of 1. Maximum length of 2048.  
Pattern: `\S*` 

## Errors
<a name="API_runtime_ListAsyncInvokes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **   
The request is denied because you do not have sufficient permissions to perform the requested action. For troubleshooting this error, see [AccessDeniedException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-access-denied) in the Amazon Bedrock User Guide  
HTTP Status Code: 403

 ** InternalServerException **   
An internal server error occurred. For troubleshooting this error, see [InternalFailure](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-internal-failure) in the Amazon Bedrock User Guide  
HTTP Status Code: 500

 ** ThrottlingException **   
Your request was denied due to exceeding the account quotas for *Amazon Bedrock*. For troubleshooting this error, see [ThrottlingException](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-throttling-exception) in the Amazon Bedrock User Guide  
HTTP Status Code: 429

 ** ValidationException **   
The input fails to satisfy the constraints specified by *Amazon Bedrock*. For troubleshooting this error, see [ValidationError](https://docs.aws.amazon.com/bedrock/latest/userguide/troubleshooting-api-error-codes.html#ts-validation-error) in the Amazon Bedrock User Guide  
HTTP Status Code: 400

## See Also
<a name="API_runtime_ListAsyncInvokes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bedrock-runtime-2023-09-30/ListAsyncInvokes) 
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-runtime-2023-09-30/ListAsyncInvokes) 