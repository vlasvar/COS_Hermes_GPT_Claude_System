/**
 * Chief of Staff System — Google Sheets provisioner.
 * @OnlyCurrentDoc
 *
 * Optional fallback for users who prefer to create a blank Google Sheet.
 * Run provisionChiefOfStaffSystem from a script bound to that Sheet.
 */
function provisionChiefOfStaffSystem() {
  const spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  const schema = getChiefOfStaffSchema_();

  schema.forEach(definition => {
    let sheet = spreadsheet.getSheetByName(definition.name);
    if (!sheet) sheet = spreadsheet.insertSheet(definition.name);

    if (sheet.getMaxColumns() < definition.columns.length) {
      sheet.insertColumnsAfter(
        sheet.getMaxColumns(),
        definition.columns.length - sheet.getMaxColumns()
      );
    }

    const existingHeaders = sheet
      .getRange(1, 1, 1, definition.columns.length)
      .getValues()[0];
    const isBlank = existingHeaders.every(value => value === '');
    const matchesSchema = definition.columns.every(
      (column, index) => existingHeaders[index] === column
    );

    if (!isBlank && !matchesSchema) {
      throw new Error(
        `Tab "${definition.name}" already exists with different headers. ` +
        'No data was changed.'
      );
    }

    sheet.getRange(1, 1, 1, definition.columns.length)
      .setValues([definition.columns])
      .setFontWeight('bold')
      .setFontColor('#FFFFFF')
      .setBackground('#2855D9');
    sheet.setFrozenRows(1);
    sheet.autoResizeColumns(1, definition.columns.length);
    if (!sheet.getFilter()) {
      sheet
        .getRange(1, 1, Math.max(sheet.getMaxRows(), 2), definition.columns.length)
        .createFilter();
    }
  });

  seedSystemCheck_(spreadsheet.getSheetByName('System Check'));
  spreadsheet.setActiveSheet(spreadsheet.getSheetByName('System Check'));
  SpreadsheetApp.flush();
}

function seedSystemCheck_(sheet) {
  if (sheet.getLastRow() > 1) return;
  sheet.getRange(2, 1, 3, 5).setValues([
    ['CHECK-READ', 'Read this row', 'Pending', '', 'Agent must confirm it can read the workbook.'],
    ['CHECK-WRITE', 'Write and read back', 'Pending', '', 'Replace this detail with a harmless test value, then read it back.'],
    ['CHECK-LOG', 'Write Agent Log', 'Pending', '', 'Add and verify an Agent Log entry.']
  ]);
}

function getChiefOfStaffSchema_() {
  return [
    {name: 'System Check', columns: ['Check ID','Capability','Status','Tested At','Details']},
    {name: 'Expenses', columns: ['Expense ID','Date','Merchant','Description','Amount','Currency','Category','Payment Method','Recurrence','Confidence','Status','Source Link','Notes','Updated At']},
    {name: 'Budget', columns: ['Budget ID','Period','Category','Planned Amount','Currency','Actual Amount','Variance','Status','Updated At']},
    {name: 'Recurring Costs', columns: ['Recurring ID','Merchant','Description','Amount','Currency','Frequency','Next Expected Date','Category','Status','Source Link','Updated At']},
    {name: 'Inbox', columns: ['Inbox ID','Received At','Source','Summary','Status','Proposed Destination','Evidence Link','Processed At']},
    {name: 'Projects', columns: ['Project ID','Name','Desired Outcome','Owner','Status','Review Date','Next Action ID','Evidence Link','Updated At']},
    {name: 'Actions', columns: ['Action ID','Project ID','Action','Owner','Due Date','Status','Approval State','Evidence Link','Updated At']},
    {name: 'Commitments', columns: ['Commitment ID','Direction','Party','Commitment','Made At','Due Date','Status','Evidence Link','Updated At']},
    {name: 'Decisions', columns: ['Decision ID','Question','Decision','Rationale','Decided At','Revisit Trigger','Evidence Link','Updated At']},
    {name: 'Contacts', columns: ['Contact ID','Display Name','Type','Context','Status','Last Interaction','Evidence Link','Updated At']},
    {name: 'Reviews', columns: ['Review ID','Period Start','Period End','Summary','Risks','Priorities','Created At','Evidence Link']},
    {name: 'Agent Log', columns: ['Log ID','Timestamp','Agent','Operation','Target Type','Target ID','Approval State','Result','Evidence Link']}
  ];
}
