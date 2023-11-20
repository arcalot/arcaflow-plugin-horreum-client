# Horreum Client Plugin Project

## Image Building

You can change this plugin's image version tag in
`.github/workflows/carpenter.yaml` by editing the
`IMAGE_TAG` variable, and pushing that change to the
branch designated in that workflow.

# Autogenerated Input/Output Documentation by Arcaflow-Docsgen Below

<!-- Autogenerated documentation by arcaflow-docsgen -->
## Horreum Client (`horreum-client`)

Uploads an object to the Horreum server

### Input

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>InputParams</td></tr>
<tr><th>Properties</th><td><details><summary>data_object (<code>
    any</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>data object for upload</td></tr><tr><th>Description:</th><td>Data object to be uploaded to the Horreum server</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>
    any</code></td></tbody></table>
            </details><details><summary>horreum_keycloak_url (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>horreum keycloak url</td></tr><tr><th>Description:</th><td>Base URL for the Horreum Keycloak server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Must match pattern:</th><td><code>((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]&#43;\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&amp;\/\?\:@\-_=#])*</code></td></tr></tbody></table>
            </details><details><summary>horreum_password (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>horreum password</td></tr><tr><th>Description:</th><td>Password for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>horreum_url (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>horreum url</td></tr><tr><th>Description:</th><td>Base URL for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Must match pattern:</th><td><code>((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]&#43;\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&amp;\/\?\:@\-_=#])*</code></td></tr></tbody></table>
            </details><details><summary>horreum_username (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>horreum username</td></tr><tr><th>Description:</th><td>Username for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>test_access_rights (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>test access rights</td></tr><tr><th>Description:</th><td>Access rights for the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>test_name (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>test name</td></tr><tr><th>Description:</th><td>Name of the target test in Horreum for the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>test_owner (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>test owner</td></tr><tr><th>Description:</th><td>Owner of the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>test_start_time (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>test start time</td></tr><tr><th>Description:</th><td>Datetime formatted start time for the object being uploaded. Can also be provided as a JSONPath to a key in the document.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details><details><summary>test_stop_time (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>test stop time</td></tr><tr><th>Description:</th><td>Datetime formatted stop time for the object being uploaded. Can also be provided as a JSONPath to a key in the document.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>InputParams (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>data_object (<code>
    any</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>data object for upload</td></tr><tr><th>Description:</th><td>Data object to be uploaded to the Horreum server</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>
    any</code></td></tbody></table>
        </details><details><summary>horreum_keycloak_url (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>horreum keycloak url</td></tr><tr><th>Description:</th><td>Base URL for the Horreum Keycloak server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Must match pattern:</th><td><code>((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]&#43;\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&amp;\/\?\:@\-_=#])*</code></td></tr></tbody></table>
        </details><details><summary>horreum_password (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>horreum password</td></tr><tr><th>Description:</th><td>Password for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>horreum_url (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>horreum url</td></tr><tr><th>Description:</th><td>Base URL for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td><tr><th>Must match pattern:</th><td><code>((http|https)\:\/\/)?[a-zA-Z0-9\.\/\?\:@\-_=#]&#43;\.([a-zA-Z]){2,6}([a-zA-Z0-9\.\&amp;\/\?\:@\-_=#])*</code></td></tr></tbody></table>
        </details><details><summary>horreum_username (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>horreum username</td></tr><tr><th>Description:</th><td>Username for the Horreum server.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>test_access_rights (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>test access rights</td></tr><tr><th>Description:</th><td>Access rights for the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>test_name (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>test name</td></tr><tr><th>Description:</th><td>Name of the target test in Horreum for the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>test_owner (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>test owner</td></tr><tr><th>Description:</th><td>Owner of the object being uploaded.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>test_start_time (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>test start time</td></tr><tr><th>Description:</th><td>Datetime formatted start time for the object being uploaded. Can also be provided as a JSONPath to a key in the document.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details><details><summary>test_stop_time (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>test stop time</td></tr><tr><th>Description:</th><td>Datetime formatted stop time for the object being uploaded. Can also be provided as a JSONPath to a key in the document.</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

### Outputs


#### error

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>ErrorOutput</td></tr>
<tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>error</td></tr><tr><th>Description:</th><td>An error has occured</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>ErrorOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>error (<code>string</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>error</td></tr><tr><th>Description:</th><td>An error has occured</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>string</code></td></tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>

#### success

<table><tbody>
<tr><th>Type:</th><td><code>scope</code></td><tr><th>Root object:</th><td>SuccessOutput</td></tr>
<tr><th>Properties</th><td><details><summary>horreum_test_id (<code>int</code>)</summary>
                <table><tbody><tr><th>Name:</th><td>horreum test id</td></tr><tr><th>Description:</th><td>Integer ID of test uploaded into Horreum</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
            </details></td></tr>
<tr><td colspan="2"><details><summary><strong>Objects</strong></summary><details><summary>SuccessOutput (<code>object</code>)</summary>
            <table><tbody><tr><th>Type:</th><td><code>object</code></td><tr><th>Properties</th><td><details><summary>horreum_test_id (<code>int</code>)</summary>
        <table><tbody><tr><th>Name:</th><td>horreum test id</td></tr><tr><th>Description:</th><td>Integer ID of test uploaded into Horreum</td></tr><tr><th>Required:</th><td>Yes</td></tr><tr><th>Type:</th><td><code>int</code></td>
</tbody></table>
        </details></td></tr>
</tbody></table>
        </details></details></td></tr>
</tbody></table>
<!-- End of autogenerated documentation -->
