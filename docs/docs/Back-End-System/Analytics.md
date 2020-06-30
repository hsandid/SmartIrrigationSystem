---
layout: post
title: Analytics
parent: Back-End System
---

# Analytics

## Back-end Events

| API                 | Testcase                                                     |
| ------------------- | ------------------------------------------------------------ |
| Signup              | invalid mobile number syntax                                 |
| Signup              | using a mobile number associated with another account        |
| Create field        | missing one of the fields / invalid value type               |
| Create field        | missing/invalid header for authentication (authorization token) |
| Update field        | invalid field id                                             |
| Update field        | missing/invalid header for authentication (authorization token) |
| Update field        | trying to update a field for another user (unauthenticated)  |
| Update field        | missing one of the fields / invalid value type               |
| Get field           | invalid field id                                             |
| Get field           | trying to read a field for another user (unauthenticated)    |
| Get field           | missing/invalid header for authentication (authorization token) |
| Get all fields      | missing/invalid header for authentication (authorization token) |
| Delete field        | invalid field id                                             |
| Delete field        | missing/invalid header for authentication (authorization token) |
| Delete field        | trying to delete a field for another user (unauthenticated)  |
| Delete field        | missing one of the fields / invalid value type               |
| Create irrigation   | invalid field id                                             |
| Create irrigation   | missing one of the fields / invalid value type               |
| Create irrigation   | missing actual irrigation attributes when &quot;watered&quot; is true |
| Update irrigation   | invalid field id                                             |
| Update irrigation   | missing one of the fields / invalid value type               |
| Update irrigation   | missing actual irrigation attributes when &quot;watered&quot; is true |
| Get irrigation      | invalid irrigation id                                        |
| Get all irrigations | invalid field id                                             |
| ET of coordinates   | invalid or missing latitude or longitude                     |
| ET of coordinates   | latitude or longitude outside of range of tiff file          |

## Front-end Events

| API               | Testcases                                                    |
| ----------------- | ------------------------------------------------------------ |
| Registration      | user enters invalid mobile number/doesn&#39;t enter mobile number |
| Registration      | user enters mobile number that belongs to another account    |
| Registration      | user enters name of town that is not available               |
| Create field      | user enters invalid values/missing values                    |
| Create field      | user attempts to create more than one field on registration  |
| ET of coordinates | user presses outside the area covered by the tiff file       |
| Arabization       | test all pages and functionalities in app in Arabic          |
| Homepage          | user wants to add a new field                                |