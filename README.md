# IMDB API Clone With DRF
<br>

<b>1. Admin Access</b>
<ul>
    <li>Admin Section: http://127.0.0.1:8000/admin/</li>
</ul>
<br>

<b>2. Accounts</b>
<ul>
    <li>Registration: http://127.0.0.1:8000/account/register/</li>
    <li>Login: http://127.0.0.1:8000/account/login/</li>
    <li>Logout: http://127.0.0.1:8000/account/logout/</li>
</ul>
<br>

<b>3. Stream Platforms</b>
<ul>
    <li>Create Element & Access List: http://127.0.0.1:8000/api/stream/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/stream/&lt;int:streamplatform_id&gt;/</li>

</ul>
<br>

<b>4. Watch List</b>
<ul>
    <li>Create & Access List: http://127.0.0.1:8000/api/</li>
    <li>Access, Update & Destroy Individual Element: http://127.0.0.1:8000/api/&lt;int:movie_id&gt;/</li>
</ul>
<br>

<b>5. Reviews</b>
<ul>
    <li>Create Review For Specific Movie: http://127.0.0.1:8000/api/&lt;int:movie_id&gt;/reviews/create/</li>
    <li>List Of All Reviews For Specific Movie: http://127.0.0.1:8000/api/&lt;int:movie_id&gt;/reviews/</li>
    <li>Access, Update & Destroy Individual Review: http://127.0.0.1:8000/api/reviews/&lt;int:review_id&gt;/</li>
</ul>
<br>

<b>6. User Review</b>
<ul>
    <li>Access All Reviews For Specific User: http://127.0.0.1:8000/api/user-reviews/?username=example</li>
</ul>
<br>
