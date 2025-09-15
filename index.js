// Google Apps Script Code - Code.gs

// 1. Enter sheet name where data is to be appended.
const sheetName = 'Sheet1'; 
// 2. Enter email address to receive submission notifications.
const emailAddress = 'tejas.patiltp2802@gmail.com'; 

const scriptProp = PropertiesService.getScriptProperties();

// This function is triggered when the form on your website is submitted (HTTP POST request).
function doPost(e) {
  const lock = LockService.getScriptLock();
  lock.tryLock(10000);

  try {
    const doc = SpreadsheetApp.openById(scriptProp.getProperty('key'));
    const sheet = doc.getSheetByName(sheetName);

    const headers = sheet.getRange(1, 1, 1, sheet.getLastColumn()).getValues()[0];
    const newRow = headers.map(function(header) {
      return header === 'Timestamp' ? new Date() : e.parameter[header];
    });

    sheet.getRange(sheet.getLastRow() + 1, 1, 1, newRow.length).setValues([newRow]);
    
    // Send an email notification
    if (emailAddress) {
      MailApp.sendEmail(emailAddress, "New Portfolio Form Submission", "You have a new registration from: " + e.parameter['Name']);
    }

    return ContentService
      .createTextOutput(JSON.stringify({ 'result': 'success', 'row': sheet.getLastRow() }))
      .setMimeType(ContentService.MimeType.JSON);

  } catch (e) {
    return ContentService
      .createTextOutput(JSON.stringify({ 'result': 'error', 'error': e }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

function setup() {
  const activeSpreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  scriptProp.setProperty('key', activeSpreadsheet.getId());
}